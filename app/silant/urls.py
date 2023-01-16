from django.urls import path

from silant.views import Index, MachineDetail, MaintenanceCreateView, ClaimCreateView, MachineCreateView, \
    LookupsListView, LookupVehicleModelListView, LookupVehicleModelUpdateView, LookupVehicleModelCreateView, \
    LookupVehicleModelDeleteView

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

]
