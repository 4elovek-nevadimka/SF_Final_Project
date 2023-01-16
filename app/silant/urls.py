from django.urls import path

from silant.views import Index, MachineDetail, MaintenanceCreateView, ClaimCreateView, MachineCreateView, \
    LookupsListView, LookupVehicleModelListView, LookupVehicleModelUpdateView, LookupVehicleModelCreateView, \
    LookupVehicleModelDeleteView, LookupEngineModelListView, LookupEngineModelCreateView, LookupEngineModelUpdateView, \
    LookupEngineModelDeleteView, LookupTransmissionModelCreateView, LookupTransmissionModelListView, \
    LookupTransmissionModelUpdateView, LookupTransmissionModelDeleteView, LookupDriveAxleModelListView, \
    LookupDriveAxleModelCreateView, LookupDriveAxleModelUpdateView, LookupDriveAxleModelDeleteView, \
    LookupSteeringBridgeModelListView, LookupSteeringBridgeModelCreateView, LookupSteeringBridgeModelUpdateView, \
    LookupSteeringBridgeModelDeleteView, LookupMaintenanceTypeListView, LookupMaintenanceTypeCreateView, \
    LookupMaintenanceTypeUpdateView, LookupMaintenanceTypeDeleteView, LookupFailureNodeListView, \
    LookupFailureNodeCreateView, LookupFailureNodeUpdateView, LookupFailureNodeDeleteView, LookupRecoveryMethodListView, \
    LookupRecoveryMethodCreateView, LookupRecoveryMethodUpdateView, LookupRecoveryMethodDeleteView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('machine/<int:pk>/', MachineDetail.as_view(), name='machine_detail'),

    path('machine_create/', MachineCreateView.as_view(), name='machine_create'),
    path('maintenance_create/', MaintenanceCreateView.as_view(), name='maintenance_create'),
    path('claim_create/', ClaimCreateView.as_view(), name='claim_create'),

    path('lookups_list/', LookupsListView.as_view(), name='lookups_list'),

    path('lookup_vehicle_model/', LookupVehicleModelListView.as_view(), name='lookup_vehicle_model'),
    path('lookup_vehicle_model_create', LookupVehicleModelCreateView.as_view(), name='lookup_vehicle_model_create'),
    path('lookup_vehicle_model_update/<int:pk>/',
         LookupVehicleModelUpdateView.as_view(), name='lookup_vehicle_model_update'),
    path('lookup_vehicle_model_delete/<int:pk>/',
         LookupVehicleModelDeleteView.as_view(), name='lookup_vehicle_model_delete'),

    path('lookup_engine_model/', LookupEngineModelListView.as_view(), name='lookup_engine_model'),
    path('lookup_engine_model_create', LookupEngineModelCreateView.as_view(), name='lookup_engine_model_create'),
    path('lookup_engine_model_update/<int:pk>/',
         LookupEngineModelUpdateView.as_view(), name='lookup_engine_model_update'),
    path('lookup_engine_model_delete/<int:pk>/',
         LookupEngineModelDeleteView.as_view(), name='lookup_engine_model_delete'),

    path('lookup_transmission_model/', LookupTransmissionModelListView.as_view(), name='lookup_transmission_model'),
    path('lookup_transmission_model_create',
         LookupTransmissionModelCreateView.as_view(), name='lookup_transmission_model_create'),
    path('lookup_transmission_model_update/<int:pk>/',
         LookupTransmissionModelUpdateView.as_view(), name='lookup_transmission_model_update'),
    path('lookup_transmission_model_delete/<int:pk>/',
         LookupTransmissionModelDeleteView.as_view(), name='lookup_transmission_model_delete'),

    path('lookup_drive_axle_model/', LookupDriveAxleModelListView.as_view(), name='lookup_drive_axle_model'),
    path('lookup_drive_axle_model_create',
         LookupDriveAxleModelCreateView.as_view(), name='lookup_drive_axle_model_create'),
    path('lookup_drive_axle_model_update/<int:pk>/',
         LookupDriveAxleModelUpdateView.as_view(), name='lookup_drive_axle_model_update'),
    path('lookup_drive_axle_model_delete/<int:pk>/',
         LookupDriveAxleModelDeleteView.as_view(), name='lookup_drive_axle_model_delete'),

    path('lookup_steering_bridge_model/',
         LookupSteeringBridgeModelListView.as_view(), name='lookup_steering_bridge_model'),
    path('lookup_steering_bridge_model_create',
         LookupSteeringBridgeModelCreateView.as_view(), name='lookup_steering_bridge_model_create'),
    path('lookup_steering_bridge_model_update/<int:pk>/',
         LookupSteeringBridgeModelUpdateView.as_view(), name='lookup_steering_bridge_model_update'),
    path('lookup_steering_bridge_model_delete/<int:pk>/',
         LookupSteeringBridgeModelDeleteView.as_view(), name='lookup_steering_bridge_model_delete'),

    path('lookup_maintenance_type/', LookupMaintenanceTypeListView.as_view(), name='lookup_maintenance_type'),
    path('lookup_maintenance_type_create',
         LookupMaintenanceTypeCreateView.as_view(), name='lookup_maintenance_type_create'),
    path('lookup_maintenance_type_update/<int:pk>/',
         LookupMaintenanceTypeUpdateView.as_view(), name='lookup_maintenance_type_update'),
    path('lookup_maintenance_type_delete/<int:pk>/',
         LookupMaintenanceTypeDeleteView.as_view(), name='lookup_maintenance_type_delete'),

    path('lookup_failure_node/', LookupFailureNodeListView.as_view(), name='lookup_failure_node'),
    path('lookup_failure_node_create', LookupFailureNodeCreateView.as_view(), name='lookup_failure_node_create'),
    path('lookup_failure_node_update/<int:pk>/',
         LookupFailureNodeUpdateView.as_view(), name='lookup_failure_node_update'),
    path('lookup_failure_node_delete/<int:pk>/',
         LookupFailureNodeDeleteView.as_view(), name='lookup_failure_node_delete'),

    path('lookup_recovery_method/', LookupRecoveryMethodListView.as_view(), name='lookup_recovery_method'),
    path('lookup_recovery_method_create',
         LookupRecoveryMethodCreateView.as_view(), name='lookup_recovery_method_create'),
    path('lookup_recovery_method_update/<int:pk>/',
         LookupRecoveryMethodUpdateView.as_view(), name='lookup_recovery_method_update'),
    path('lookup_recovery_method_delete/<int:pk>/',
         LookupRecoveryMethodDeleteView.as_view(), name='lookup_recovery_method_delete'),
]
