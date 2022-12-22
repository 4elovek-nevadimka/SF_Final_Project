import csv
from datetime import datetime

from django.contrib.auth.models import Permission, Group

from silant.models import Machine, Maintenance, MaintenanceType, User


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
            dbTable.objects.create(
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
    pass
    # Machine.objects.create(
    #
    # )
    # print('\n'.join(row[14].split(';')))


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
    pass
