
# Справочники для основных сущностей: Машина, Техническое обслуживание (ТО), Рекламация

vehicle_models = [
    {
        'name': 'ПД1,5',
        'description': 'Описание для ПД1,5'
    },
    {
        'name': 'ПД5,0',
        'description': 'Описание для ПД5,0'
    },
    {
        'name': 'ПД3,0',
        'description': 'Описание для ПД3,0'
    },
    {
        'name': 'ПГ1,5',
        'description': 'Описание для ПГ1,5'
    },
    {
        'name': 'ПД2,0',
        'description': 'Описание для ПД2,0'
    },
    {
        'name': 'ПД2,5',
        'description': 'Описание для ПД2,5'
    },
]

engine_models = [
    {
        'name': 'Kubota D1803',
        'description': 'Описание для Kubota D1803'
    },
    {
        'name': 'ММЗ Д-243',
        'description': 'Описание для ММЗ Д-243'
    },
    {
        'name': 'Kubota V3300',
        'description': 'Описание для Kubota V3300'
    },
    {
        'name': 'Nissan K21',
        'description': 'Описание для Nissan K21'
    },
    {
        'name': 'MMZ-4D',
        'description': 'Описание для MMZ-4D'
    },
]

transmission_models = [
    {
        'name': '10VA-00105',
        'description': 'Описание для 10VA-00105'
    },
    {
        'name': 'HF50-VP020',
        'description': 'Описание для HF50-VP020'
    },
    {
        'name': '10VB-00106',
        'description': 'Описание для 10VB-00106'
    },
    {
        'name': 'HF30-VP010',
        'description': 'Описание для HF30-VP010'
    },
]

drive_axle_models = [
    {
        'name': '20VA-00101',
        'description': 'Описание для 20VA-00101'
    },
    {
        'name': 'HA50-VP010',
        'description': 'Описание для HA50-VP010'
    },
    {
        'name': '20VB-00102',
        'description': 'Описание для 20VB-00102'
    },
    {
        'name': 'HA30-02020',
        'description': 'Описание для HA30-02020'
    },
]

steering_bridge_models = [
    {
        'name': 'VS20-00001',
        'description': 'Описание для VS20-00001'
    },
    {
        'name': 'B350655A',
        'description': 'Описание для B350655A'
    },
    {
        'name': 'VS30-00001',
        'description': 'Описание для VS30-00001'
    },
]

maintenance_types = [
    {
        'name': 'ТО-0 (50 м/час)',
        'description': 'Описание для ТО-0 (50 м/час)'
    },
    {
        'name': 'ТО-1 (200 м/час)',
        'description': 'Описание для ТО-1 (200 м/час)'
    },
    {
        'name': 'ТО-2 (400 м/час)',
        'description': 'Описание для ТО-2 (400 м/час)'
    },
    {
        'name': 'ТО-4 (1000м/час)',
        'description': 'Описание для ТО-4 (1000м/час)'
    },
    {
        'name': 'ТО-5 (2000м/час)',
        'description': 'Описание для ТО-5 (2000м/час)'
    },
]

failure_nodes = [
    {
        'name': 'Двигатель',
        'description': 'Описание для Двигатель'
    },
    {
        'name': 'Трансмиссия',
        'description': 'Описание для Трансмиссия'
    },
    {
        'name': 'Ведущий мост',
        'description': 'Описание для Ведущий мост'
    },
    {
        'name': 'Управляемый мост',
        'description': 'Описание для Управляемый мост'
    },
    {
        'name': 'Подъёмное устройство',
        'description': 'Описание для Подъёмное устройство'
    },
    {
        'name': 'Гидросистема',
        'description': 'Описание для Гидросистема'
    },
]

recovery_methods = [
    {
        'name': 'Ремонт узла',
        'description': 'Описание для Ремонт узла'
    },
    {
        'name': 'Замена узла',
        'description': 'Описание для Замена узла'
    },
]


# Пользователи: клиенты, сервисные компании, менеджеры


clients = [
    {
        'username': 'user_cl_1',
        'password': '1',
        'name': 'ИП Трудников С.В.',
        'description': 'Описание для ИП Трудников С.В.',
        'role': 'CL',
    },
    {
        'username': 'user_cl_2',
        'password': '1',
        'name': 'ООО "ФПК21"',
        'description': 'Описание для ООО "ФПК21"',
        'role': 'CL',
    },
    {
        'username': 'user_cl_3',
        'password': '1',
        'name': 'ООО "МНС77"',
        'description': 'Описание для ООО "МНС77"',
        'role': 'CL',
    },
    {
        'username': 'user_cl_4',
        'password': '1',
        'name': 'ООО "Ранский ЛПХ"',
        'description': 'Описание для ООО "Ранский ЛПХ"',
        'role': 'CL',
    },
    {
        'username': 'user_cl_5',
        'password': '1',
        'name': 'ООО "Комплект-Поставка"',
        'description': 'Описание для ООО "Комплект-Поставка"',
        'role': 'CL',
    },
    {
        'username': 'user_cl_6',
        'password': '1',
        'name': 'ООО "РМК"',
        'description': 'Описание для ООО "РМК"',
        'role': 'CL',
    },
    {
        'username': 'user_cl_7',
        'password': '1',
        'name': 'АО "Зандер"',
        'description': 'Описание для АО "Зандер"',
        'role': 'CL',
    },
]

service_companies = [
    {
        'username': 'user_sc_1',
        'password': '1',
        'name': 'ООО "Промышленная техника"',
        'description': 'Описание для ООО "Промышленная техника"',
        'role': 'SC',
    },
    {
        'username': 'user_sc_2',
        'password': '1',
        'name': 'ООО "Силант"',
        'description': 'Описание для ООО "Силант"',
        'role': 'SC',
    },
    {
        'username': 'user_sc_3',
        'password': '1',
        'name': 'ООО "ФНС"',
        'description': 'Описание для ООО "ФНС"',
        'role': 'SC',
    },
    {
        'username': 'user_sc_4',
        'password': '1',
        'name': 'самостоятельно',
        'description': 'Описание для самостоятельно',
        'role': 'SC',
    },
]

managers = [
    {
        'username': 'user_mn_1',
        'password': '1',
        'name': 'Иванов О.П',
        'description': 'Главный менеджер',
        'role': 'MN',
    },
    {
        'username': 'user_mn_2',
        'password': '1',
        'name': 'Петров С.Л',
        'description': 'Менеджер по отгрузкам',
        'role': 'MN',
    },
]


# Разрешения для групп: клиент, сервисная компания, менеджер


client_permission_list = (
    'view_machine', 'view_maintenance', 'view_claim',
    'add_maintenance',
)

service_company_permission_list = (
    'view_machine', 'view_maintenance', 'view_claim',
    'add_maintenance', 'add_claim',
)

manager_permission_list = (
    'view_machine', 'view_maintenance', 'view_claim',
    'add_machine', 'add_maintenance', 'add_claim',

    # права на создание / редактирование справочников
    'view_vehicle_model', 'add_vehicle_model', 'change_vehicle_model', 'delete_vehicle_model',
    'view_engine_model', 'add_engine_model', 'change_engine_model', 'delete_engine_model',
    'view_transmission_model', 'add_transmission_model', 'change_transmission_model', 'delete_transmission_model',
    'view_drive_axle_model', 'add_drive_axle_model', 'change_drive_axle_model', 'delete_drive_axle_model',
    'view_steering_bridge_model', 'add_steering_bridge_model', 'change_steering_bridge_model',
    'delete_steering_bridge_model',

    'view_maintenance_type', 'add_maintenance_type', 'change_maintenance_type', 'delete_maintenance_type',

    'view_failure_node', 'add_failure_node', 'change_failure_node', 'delete_failure_node',
    'view_recovery_method', 'add_recovery_method', 'change_recovery_method', 'delete_recovery_method',
)
