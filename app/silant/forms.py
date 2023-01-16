from django.contrib.auth import get_user_model
from django.forms import ModelForm, DateInput

from silant.models import Maintenance, Claim, Machine, VehicleModel, EngineModel, TransmissionModel, DriveAxleModel, \
    SteeringBridgeModel, MaintenanceType


class MachineForm(ModelForm):
    class Meta:
        model = Machine
        fields = '__all__'
        exclude = ('client',)
        widgets = {
            'shipment_date': DateInput(
                format='%d/%m/%Y',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(MachineForm, self).__init__(*args, **kwargs)
        self.fields['service_company'].queryset = get_user_model().objects.filter(role='SC')


class MaintenanceForm(ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'

        widgets = {
            'maintenance_date': DateInput(
                format='%d/%m/%Y',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'}),
            'work_order_date': DateInput(
                format='%d/%m/%Y',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(MaintenanceForm, self).__init__(*args, **kwargs)
        self.fields['service_company'].queryset = get_user_model().objects.filter(role='SC')


class ClaimForm(ModelForm):
    class Meta:
        model = Claim
        fields = '__all__'

        widgets = {
            'failure_date': DateInput(
                format='%d/%m/%Y',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'}),
            'recovery_date': DateInput(
                format='%d/%m/%Y',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'})
        }


class VehicleModelForm(ModelForm):
    class Meta:
        model = VehicleModel
        fields = '__all__'


class EngineModelForm(ModelForm):
    class Meta:
        model = EngineModel
        fields = '__all__'


class TransmissionModelForm(ModelForm):
    class Meta:
        model = TransmissionModel
        fields = '__all__'


class DriveAxleModelForm(ModelForm):
    class Meta:
        model = DriveAxleModel
        fields = '__all__'


class SteeringBridgeModelForm(ModelForm):
    class Meta:
        model = SteeringBridgeModel
        fields = '__all__'


class MaintenanceTypeForm(ModelForm):
    class Meta:
        model = MaintenanceType
        fields = '__all__'
