import json
from typing import List, Optional, Tuple
import shlex
from datetime import datetime
import subprocess
from . import helpers, steps
from pathlib import Path



def database_list(project: str, instance_id: str, simulate: bool = False) -> List[str]:
    command = f'gcloud sql databases list --project="{project}" --instance="{instance_id}" --format=json'
    if simulate:
        data = '[{"name": "mysql", "name": "db-a"}]'
    else:
        p = subprocess.run(shlex.split(command), stdout=subprocess.PIPE)
        data = p.stdout.decode('utf-8')

    data = json.loads(data)
    data = [x.get('name') for x in data]
    data = [x for x in data if x not in [
        "mysql", "information_schema", "performance_schema", None, "sys"
    ]]

    return data


def unpack_db_name(name: Optional[str]) -> Tuple[bool,str,str,str,str]:
    if name is None:
        print(helpers.bcolors.FAIL +
              'Insert a SQL Instanz connection string like <project>:<region>:<instance-id>' + helpers.bcolors.ENDC)
        return False,None,None,None,None

    values = name.split(':')
    if len(values) not in [3,4]:
        print(helpers.bcolors.FAIL +
              'Insert a SQL Instanz connection string like <project>:<region>:<instance-id>' + helpers.bcolors.ENDC)
        return False,None,None,None,None

    project = values[0]
    region = values[1]
    instance_id = values[2]
    try:
        db = values[3]
    except IndexError:
        db = None
    return True, project, region, instance_id, db

def instances_list(config) -> List[str]:
    databases = [x.get("databases") for x in config.load_projects()]
    databases = [x for x in databases if x is not None]
    databases = [item for sublist in databases for item in sublist]
    databases = [x for x in databases if x.strip().startswith('sql:')]
    databases = [x for x in databases if len(x.split(':')) == 5]
    databases = {":".join(x.split(':')[1:-1]) for x in databases}
    return databases


def cli_main(args, config) -> int:
    if args.action == 'sql-init':
        is_success, project, region, instance_id,_ = unpack_db_name(args.name)
        if not is_success:
            return 1

        bucket_name = f"{instance_id.lower()}-db-exports"

        print(f'- Bucket gs://{bucket_name} wird angelegt')
        manager = steps.Manager(config, [
            steps.StepCommand(
                shlex.split(
                    f"gcloud storage buckets create gs://{bucket_name} --project='{project}' --location='{region}'"),
                can_fail=True,
                retry=0,
            ),
        ], simulate=args.simulate)
        rc = manager.run()
        if rc != 0:
            return rc

        print('- dem Dienstkonto des SQL Servers Administrator Rechte für Storage im Bucket geben')
        print('- im Bucket den Lebenszyklus einstellen, das die Dateien nach 14 Tagen gelöscht werden')
        print(
            f'https://console.cloud.google.com/storage/browser/{bucket_name};tab=lifecycle?project={project}')

    elif args.action == 'sql-list-instances':
        instances = instances_list(config)

        for instance in instances:
            print(f"- {instance}")

    elif args.action == 'sql-list-databases':
        is_success, project, region, instance_id, _ = unpack_db_name(args.name)
        if not is_success:
            return 1

        databases = database_list(project, instance_id, args.simulate)
        print(databases)
    elif args.action == 'sql-dump':
        if args.name is not None:    
            is_success, project, region, instance_id,db = unpack_db_name(args.name)
            if not is_success:
                return 1
            if db is not None:
                databases = [db]
            else:
                databases = database_list(project, instance_id, args.simulate)
            for db in databases:
                now = datetime.now()
                name = args.name.lower().replace(':', '-')
                bucket_name = f"{instance_id.lower()}-db-exports"
                backup_name = f"{now.strftime('%Y-%m-%d')}/{name}_{db}.sql"

                manager = steps.Manager(config, [
                    steps.StepCommand(
                        shlex.split(
                            f"gcloud sql export sql {instance_id} gs://{bucket_name}/{backup_name} --database='{db}' --project='{project}'"),
                    ),
                ], simulate=args.simulate)
                rc = manager.run()
                if rc != 0:
                    print("Fehler die auftreten können:")
                    print(
                        "- keine Rechte, dann bitte das SQL Instanz Dienstkonto mit zu den Storage Rechten für das Bucket hinzufügem.")
                    return rc
        else:
            instances = instances_list(config)
            for instance in instances:
                is_success, project, region, instance_id, _ = unpack_db_name(instance)
                if not is_success:
                    return 1
                databases = database_list(project, instance_id, args.simulate)
                for db in databases:
                    now = datetime.now()
                    bucket_name = f"{instance_id.lower()}-db-exports"
                    backup_name = f"{now.strftime('%Y-%m-%d')}/{project}-{region}-{instance_id}_{db}.sql"

                    manager = steps.Manager(config, [
                        steps.StepCommand(
                            shlex.split(
                                f"gcloud sql export sql {instance_id} gs://{bucket_name}/{backup_name} --database='{db}' --project='{project}'"),
                        ),
                    ], simulate=args.simulate)
                    rc = manager.run()
                    if rc != 0:
                        print("Ein Fehler ist aufgetreten.")
                        return rc
    elif args.action == 'sql-download':
        
        instances = instances_list(config)

        for instance in instances:
            print(f"- {instance}")
            is_success, project, region, instance_id, _ = unpack_db_name(instance)

            bucket_name = f"{instance_id.lower()}-db-exports"
            
            backup_path = f"~/db_dumps/{bucket_name}"
        
            manager = steps.Manager(config, [
                steps.StepCommand(
                    shlex.split(
                        f"mkdir -p {backup_path}"
                    ),
                    can_fail=True,
                    retry=0,
                ),
                steps.StepCommand(
                    shlex.split(
                        f"gsutil rsync -r gs://{bucket_name}/ {backup_path}"
                    ),
                    can_fail=True,
                    retry=0,
                ),
            ], simulate=args.simulate)
            rc = manager.run()
            if rc != 0:
                return rc
    elif args.action == 'sql-push-to-drive':
        
        destination = args.name
        destination_path = Path(destination)
        if not destination_path.exists():
            print(helpers.bcolors.FAIL + f"Path not exists: {destination}" + helpers.bcolors.ENDC)
        
        manager = steps.Manager(config, [
                steps.StepCommand(
                    shlex.split(
                        f"rsync -av --ignore-existing ~/db_dumps/ {destination}"
                    ),
                    can_fail=True,
                    retry=0,
                ),
        ], simulate=args.simulate)
        rc = manager.run()
        if rc != 0:
            return rc
        
        
    return 0
