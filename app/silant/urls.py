from django.urls import path

from silant.views import Index, MachineDetail, MaintenanceCreateView, ClaimCreateView, MachineCreateView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('machine/<int:pk>/', MachineDetail.as_view(), name='machine_detail'),

    path('machine_create/', MachineCreateView.as_view(), name='machine_create'),
    path('maintenance_create/', MaintenanceCreateView.as_view(), name='maintenance_create'),
    path('claim_create/', ClaimCreateView.as_view(), name='claim_create'),

]
