from django.contrib import admin

from silant.models import *

admin.site.register(User)

admin.site.register(Machine)
admin.site.register(Maintenance)
admin.site.register(Claim)

admin.site.register(VehicleModel)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(DriveAxleModel)
admin.site.register(SteeringBridgeModel)

admin.site.register(MaintenanceType)
admin.site.register(FailureNode)
admin.site.register(RecoveryMethod)
