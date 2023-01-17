from django_filters import FilterSet

from .models import Machine, Maintenance, Claim


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
    class Meta:
        model = Maintenance
        fields = ('maintenance_type',
                  'machine__serial_number',
                  'service_company',)

    def __init__(self, *args, **kwargs):
        super(MaintenanceFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()


class ClaimFilter(FilterSet):
    class Meta:
        model = Claim
        fields = ('failure_node',
                  'recovery_method',
                  'machine__service_company',)

    def __init__(self, *args, **kwargs):
        super(ClaimFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()
