from django.contrib.auth.models import Permission, Group


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
