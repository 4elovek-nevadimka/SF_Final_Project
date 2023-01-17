from django_filters import FilterSet, CharFilter, ModelChoiceFilter

from .models import Machine, Maintenance, Claim, User


class GuestFilter(FilterSet):
    class Meta:
        model = Machine
        fields = ('serial_number',)

    def __init__(self, *args, **kwargs):
        super(GuestFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()


class MachineFilter(FilterSet):
    class Meta:
        model = Machine
        fields = ('vehicle_model',
                  'engine_model',
                  'transmission_model',
                  'drive_axle_model',
                  'steering_bridge_model',)

    def __init__(self, *args, **kwargs):
        super(MachineFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()


class MaintenanceFilter(FilterSet):
    serial_number = CharFilter(label='Заводской номер машины',
                               field_name='machine__serial_number',)
    service_company = ModelChoiceFilter(label='Сервисная компания',
                                        field_name='machine__service_company',
                                        queryset=User.objects.filter(role='SC'))

    class Meta:
        model = Maintenance
        fields = ('maintenance_type',
                  'service_company',
                  'serial_number',)

    def __init__(self, *args, **kwargs):
        super(MaintenanceFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()


class ClaimFilter(FilterSet):
    service_company = ModelChoiceFilter(label='Сервисная компания',
                                        field_name='machine__service_company',
                                        queryset=User.objects.filter(role='SC'))

    class Meta:
        model = Claim
        fields = ('failure_node',
                  'recovery_method',
                  'service_company',)

    def __init__(self, *args, **kwargs):
        super(ClaimFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()
