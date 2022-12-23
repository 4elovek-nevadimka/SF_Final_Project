from django.contrib import admin

from silant.models import *


@admin.register(User)
class User(admin.ModelAdmin):
    fields = ('username', 'email', 'password', 'role', 'name', 'description',)
    list_display = ('username', 'role', 'name', 'description',)
    list_filter = ('role', 'name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(Machine)
class Machine(admin.ModelAdmin):
    list_display = ('serial_number', 'vehicle_model', 'engine_model', 'transmission_model', 'drive_axle_model',
                    'steering_bridge_model', 'shipment_date', 'equipment', 'client', 'service_company',)
    list_filter = ('vehicle_model', 'engine_model', 'transmission_model', 'drive_axle_model', 'steering_bridge_model',)
    search_fields = ('serial_number',)


@admin.register(Maintenance)
class Maintenance(admin.ModelAdmin):
    list_display = ('machine', 'maintenance_type', 'maintenance_date', 'operating_time', 'work_order_number',
                    'service_company',)
    list_filter = ('maintenance_type', 'maintenance_date',)


@admin.register(Claim)
class Claim(admin.ModelAdmin):
    list_display = ('machine', 'failure_date', 'operating_time', 'failure_node', 'recovery_method', 'recovery_date',
                    'machine_downtime',)
    list_filter = ('failure_date', 'failure_node', 'recovery_method',)


admin.site.register(VehicleModel)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(DriveAxleModel)
admin.site.register(SteeringBridgeModel)

admin.site.register(MaintenanceType)
admin.site.register(FailureNode)
admin.site.register(RecoveryMethod)
