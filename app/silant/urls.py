from django.urls import path

from silant.views import Index, MachineDetail, MaintenanceCreateView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('machine/<int:pk>/', MachineDetail.as_view(), name='machine_detail'),

    path('maintenance_create/', MaintenanceCreateView.as_view(), name='maintenance_create'),
]
