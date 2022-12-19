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
