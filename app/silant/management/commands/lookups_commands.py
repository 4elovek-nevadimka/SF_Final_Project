import csv
from datetime import datetime

from django.contrib.auth.models import Permission, Group

from silant.models import Machine, Maintenance, MaintenanceType, User, VehicleModel, EngineModel, TransmissionModel, \
    DriveAxleModel, SteeringBridgeModel, Claim, FailureNode, RecoveryMethod


def fill_lookup_table(dbTable, dataArray, cmd, infoName):
    try:
        for value in dataArray:
            dbTable.objects.create(
                name=value.get('name'), description=value.get('description')
            )
        cmd.stdout.write(
            cmd.style.SUCCESS(f'Справочник "{infoName}" успешно инициализирован!'))
    except BaseException as e:
        cmd.stdout.write(cmd.style.ERROR(f'Error: {e}'))


def fill_user_lookup_table(dbTable, dataArray, cmd, infoName):
    try:
        for value in dataArray:
            dbTable.objects.create_user(
                username=value.get('username'), password=value.get('password'),
                name=value.get('name'), description=value.get('description'),
                role=value.get('role'),
            )
        cmd.stdout.write(
            cmd.style.SUCCESS(f'Справочник "{infoName}" успешно инициализирован!'))
    except BaseException as e:
        cmd.stdout.write(cmd.style.ERROR(f'Error: {e}'))


def create_group(group_name, permission_list, cmd):
    try:
        group = Group.objects.create(name=group_name)
        for permission in permission_list:
            group.permissions.add(Permission.objects.get(codename=permission))
        cmd.stdout.write(
            cmd.style.SUCCESS(f'Группа "{group_name}" успешно добавлена!'))
    except BaseException as e:
        cmd.stdout.write(cmd.style.ERROR(f'Error: {e}'))


def read_csv_file(path, cmd, info):
    try:
        with open(path, newline='') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if info == 'Машина':
                    create_machine(row)
                elif info == 'Техническое обслуживание':
                    create_maintenance(row)
                else:
                    create_claim(row)

        cmd.stdout.write(
            cmd.style.SUCCESS(f'Таблица "{info}" успешно заполнена!'))
    except BaseException as e:
        cmd.stdout.write(cmd.style.ERROR(f'Error: {e}'))


def create_machine(data):
    Machine.objects.create(
        vehicle_model=VehicleModel.objects.get(name=data[0]),
        serial_number=data[1],
        engine_model=EngineModel.objects.get(name=data[2]),
        engine_serial_number=data[3],
        transmission_model=TransmissionModel.objects.get(name=data[4]),
        transmission_serial_number=data[5],
        drive_axle_model=DriveAxleModel.objects.get(name=data[6]),
        drive_axle_serial_number=data[7],
        steering_bridge_model=SteeringBridgeModel.objects.get(name=data[8]),
        steering_bridge_serial_number=data[9],
        shipment_date=datetime.strptime(data[10], '%d.%m.%Y').date(),
        client=User.objects.get(name=data[11]),
        consumer=data[12],
        delivery_address=data[13],
        equipment='\n'.join(data[14].split(';')),
        service_company=User.objects.get(name=data[15]),
    )


def create_maintenance(data):
    pass
    Maintenance.objects.create(
        machine=Machine.objects.get(serial_number=data[0]),
        maintenance_type=MaintenanceType.objects.get(name=data[1]),
        maintenance_date=datetime.strptime(data[2], '%d.%m.%Y').date(),
        operating_time=data[3],
        work_order_number=data[4],
        work_order_date=datetime.strptime(data[5], '%d.%m.%Y').date(),
        service_company=User.objects.get(name=data[6]),
    )


def create_claim(data):
    Claim.objects.create(
        machine=Machine.objects.get(serial_number=data[0]),
        failure_date=datetime.strptime(data[1], '%d.%m.%Y').date(),
        operating_time=data[2],
        failure_node=FailureNode.objects.get(name=data[3]),
        failure_description=data[4],
        recovery_method=RecoveryMethod.objects.get(name=data[5]),
        spare_parts=data[6],
        recovery_date=datetime.strptime(data[7], '%d.%m.%Y').date(),
        machine_downtime=data[8],
    )
