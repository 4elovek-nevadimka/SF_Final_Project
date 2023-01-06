from django.urls import path

from silant.views import Index, MachineDetail

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('machine/<int:pk>/', MachineDetail.as_view(), name='machine_detail'),
]
