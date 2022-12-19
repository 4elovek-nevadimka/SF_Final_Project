from django.contrib.auth.models import AbstractUser
from django.db import models

from final_project import settings


class User(AbstractUser):
    CHOICES = (
        ('CL', 'Client'),
        ('SC', 'Service company'),
        ('MN', 'Manager')
    )
    name = models.CharField(max_length=128, null=True, blank=True, verbose_name='Название')
    description = models.CharField(max_length=512, null=True, blank=True, verbose_name='Описание')
    role = models.CharField(max_length=2, choices=CHOICES, default='CL', verbose_name='Роль')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.name}'


class Machine(models.Model):
    # Зав. № машины
    serial_number = models.CharField(max_length=32, unique=True, verbose_name='Заводской номер машины')
    # Модель техники
    vehicle_model = models.ForeignKey('VehicleModel', on_delete=models.DO_NOTHING, verbose_name='Модель техники')
    # Модель двигателя
    engine_model = models.ForeignKey('EngineModel', on_delete=models.DO_NOTHING, verbose_name='Модель двигателя')
    # Зав. № двигателя
    engine_serial_number = models.CharField(max_length=32, verbose_name='Зав. № двигателя')
    # Модель трансмиссии
    transmission_model = models.ForeignKey(
        'TransmissionModel', on_delete=models.DO_NOTHING, verbose_name='Модель трансмиссии')
    # Зав. № трансмиссии
    transmission_serial_number = models.CharField(max_length=32, verbose_name='Зав. № трансмиссии')
    # Модель ведущего моста
    drive_axle_model = models.ForeignKey(
        'DriveAxleModel', on_delete=models.DO_NOTHING, verbose_name='Модель ведущего моста')
    # Зав. № ведущего моста
    drive_axle_serial_number = models.CharField(max_length=32, verbose_name='Зав. № ведущего моста')
    # Модель управляемого моста
    steering_bridge_model = models.ForeignKey(
        'SteeringBridgeModel', on_delete=models.DO_NOTHING, verbose_name='Модель управляемого моста')
    # Зав. № управляемого моста
    steering_bridge_serial_number = models.CharField(max_length=32, verbose_name='Зав. № управляемого моста')
    # Договор поставки №, дата
    supply_contract = models.CharField(max_length=128, verbose_name='Договор поставки №, дата')
    # Дата отгрузки с завода
    shipment_date = models.DateField(verbose_name='Дата отгрузки с завода')
    # Грузополучатель (конечный потребитель)
    consumer = models.CharField(max_length=128, verbose_name='Грузополучатель (конечный потребитель)')
    # Адрес поставки (эксплуатации)
    delivery_address = models.CharField(max_length=256, verbose_name='Адрес поставки (эксплуатации)')
    # Комплектация (доп. опции)
    equipment = models.CharField(max_length=512, verbose_name='Комплектация (доп. опции)')
    # Клиент
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='client',
                               on_delete=models.DO_NOTHING, verbose_name='Клиент')
    # Сервисная компания
    service_company = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='service_company',
                                        on_delete=models.DO_NOTHING, verbose_name='Сервисная компания')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ('shipment_date',)

    def __str__(self):
        return self.vehicle_model.name


class Maintenance(models.Model):
    # Вид ТО
    maintenance_type = models.ForeignKey('MaintenanceType', on_delete=models.DO_NOTHING, verbose_name='Вид ТО')
    # Дата проведения ТО
    maintenance_date = models.DateField(verbose_name='Дата проведения ТО')
    # Наработка, м/час
    operating_time = models.PositiveIntegerField(verbose_name='Наработка, м/час')
    # № заказ-наряда
    work_order_number = models.CharField(max_length=64, verbose_name='Заказ-наряд')
    # дата заказ-наряда
    work_order_date = models.DateField(verbose_name='дата заказ-наряда')
    # Организация, проводившая ТО
    service_company = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='Сервисная компания')
    # Машина
    machine = models.ForeignKey('Machine', on_delete=models.DO_NOTHING, verbose_name='Модель техники')

    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Технические обслуживания'
        ordering = ('maintenance_date',)

    def __str__(self):
        return f'{self.machine.vehicle_model} - {self.maintenance_type}'


class Claim(models.Model):
    # Дата отказа
    failure_date = models.DateField(verbose_name='Дата отказа')
    # Наработка, м/час
    operating_time = models.PositiveIntegerField(verbose_name='Наработка, м/час')
    # Узел отказа
    failure_node = models.ForeignKey('FailureNode', on_delete=models.DO_NOTHING, verbose_name='Узел отказа')
    # Описание отказа
    failure_description = models.CharField(max_length=512,  verbose_name='Описание отказа')
    # Способ восстановления
    recovery_method = models.ForeignKey(
        'RecoveryMethod', on_delete=models.DO_NOTHING, verbose_name='Способ восстановления')
    # Используемые запасные части
    spare_parts = models.CharField(max_length=512, verbose_name='Используемые запасные части')
    # Дата восстановления
    recovery_date = models.DateField(verbose_name='Дата восстановления')
    # Время простоя техники
    machine_downtime = models.PositiveIntegerField(null=True, verbose_name='Время простоя техники')
    # Машина
    machine = models.ForeignKey('Machine', on_delete=models.DO_NOTHING, verbose_name='Модель техники')

    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'
        ordering = ('failure_date',)

    def __str__(self):
        return f'{self.machine.vehicle_model} - {self.failure_node}'


# Справочники


class VehicleModel(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'

    def __str__(self):
        return self.name


class EngineModel(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')

    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателей'

    def __str__(self):
        return self.name


class TransmissionModel(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссий'

    def __str__(self):
        return self.name


class DriveAxleModel(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модели ведущих мостов'

    def __str__(self):
        return self.name


class SteeringBridgeModel(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемых мостов'

    def __str__(self):
        return self.name


class MaintenanceType(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')

    class Meta:
        verbose_name = 'Вид ТО'
        verbose_name_plural = 'Виды ТО'

    def __str__(self):
        return self.name


class FailureNode(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')

    class Meta:
        verbose_name = 'Узел отказа'
        verbose_name_plural = 'Узлы отказа'

    def __str__(self):
        return self.name


class RecoveryMethod(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способы восстановления'

    def __str__(self):
        return self.name
