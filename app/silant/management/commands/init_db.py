from django.core.management import BaseCommand

from silant.models import VehicleModel, EngineModel, TransmissionModel, User, RecoveryMethod, FailureNode, \
    MaintenanceType, SteeringBridgeModel, DriveAxleModel
from .lookups_commands import fill_lookup_table, fill_user_lookup_table, create_group
from .lookups_data import vehicle_models, engine_models, transmission_models, drive_axle_models, \
    steering_bridge_models, maintenance_types, failure_nodes, recovery_methods, clients, service_companies, managers, \
    client_permission_list, manager_permission_list, service_company_permission_list


class Command(BaseCommand):
    help = 'Команда для заполнения БД тестовым набором данных'
    requires_migrations_checks = True

    def handle(self, *args, **options):
        self.stdout.write('Инициализация базы данных тестовым набором данных...')

        # Группы и разрешения
        create_group(
            'Client', client_permission_list, self)
        create_group(
            'Service company', service_company_permission_list, self)
        create_group(
            'Manager', manager_permission_list, self)

        # Справочники пользователей
        fill_user_lookup_table(
            User, clients, self, 'Пользователи: клиенты')
        fill_user_lookup_table(
            User, service_companies, self, 'Пользователи: сервисные компании')
        fill_user_lookup_table(
            User, managers, self, 'Пользователи: менеджеры')

        # Справочники для сущности 'Машина'
        fill_lookup_table(
            VehicleModel, vehicle_models, self, 'Модель техники')
        fill_lookup_table(
            EngineModel, engine_models, self, 'Модель двигателя')
        fill_lookup_table(
            TransmissionModel, transmission_models, self, 'Модель трансмиссии')
        fill_lookup_table(
            DriveAxleModel, drive_axle_models, self, 'Модель ведущего моста')
        fill_lookup_table(
            SteeringBridgeModel, steering_bridge_models, self, 'Модель управляемого моста')

        # Справочники для сущности 'Техническое обслуживание (ТО)'
        fill_lookup_table(
            MaintenanceType, maintenance_types, self, 'Вид ТО')

        # Справочники для сущности 'Рекламация'
        fill_lookup_table(
            FailureNode, failure_nodes, self, 'Узел отказа')
        fill_lookup_table(
            RecoveryMethod, recovery_methods, self, 'Способ восстановления')

        # Экспорт тестовых данных по сущностям Машина, Техническое обслуживание (ТО), Рекламация
