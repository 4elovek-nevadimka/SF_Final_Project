from django.urls import path

from silant.views import Index, MachineDetail, MaintenanceCreateView, ClaimCreateView, MachineCreateView, \
    LookupsListView, LookupVehicleModelListView, LookupVehicleModelUpdateView, LookupVehicleModelCreateView, \
    LookupVehicleModelDeleteView, LookupEngineModelListView, LookupEngineModelCreateView, LookupEngineModelUpdateView, \
    LookupEngineModelDeleteView, LookupTransmissionModelCreateView, LookupTransmissionModelListView, \
    LookupTransmissionModelUpdateView, LookupTransmissionModelDeleteView

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

]
