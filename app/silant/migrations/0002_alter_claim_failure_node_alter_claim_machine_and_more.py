# Generated by Django 4.1.4 on 2023-01-17 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('silant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='failure_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.failurenode', verbose_name='Узел отказа'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.machine', verbose_name='Модель техники'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='recovery_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.recoverymethod', verbose_name='Способ восстановления'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='drive_axle_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.driveaxlemodel', verbose_name='Модель ведущего моста'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='engine_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.enginemodel', verbose_name='Модель двигателя'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='service_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_company', to=settings.AUTH_USER_MODEL, verbose_name='Сервисная компания'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='steering_bridge_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.steeringbridgemodel', verbose_name='Модель управляемого моста'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='transmission_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.transmissionmodel', verbose_name='Модель трансмиссии'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='vehicle_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.vehiclemodel', verbose_name='Модель техники'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.machine', verbose_name='Модель техники'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.maintenancetype', verbose_name='Вид ТО'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='service_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Сервисная компания'),
        ),
    ]
