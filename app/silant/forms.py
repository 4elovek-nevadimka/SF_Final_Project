from django.forms import ModelForm

from silant.models import Maintenance


class MaintenanceForm(ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'
