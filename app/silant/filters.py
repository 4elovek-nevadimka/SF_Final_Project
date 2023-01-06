from django_filters import FilterSet

from .models import Machine, Maintenance, Claim


class GuestFilter(FilterSet):
    class Meta:
        model = Machine
        fields = ('serial_number',)


class MachineFilter(FilterSet):
    class Meta:
        model = Machine
        fields = ('vehicle_model',
                  'engine_model',
                  'transmission_model',
                  'drive_axle_model',
                  'steering_bridge_model',)


class MaintenanceFilter(FilterSet):
    class Meta:
        model = Maintenance
        fields = ('maintenance_type',
                  'machine__serial_number',
                  'service_company',)


class ClaimFilter(FilterSet):
    class Meta:
        model = Claim
        fields = ('failure_node',
                  'recovery_method',
                  'machine__service_company',)
