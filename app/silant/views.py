from django.views.generic import ListView

from silant.filters import GuestFilter, MachineFilter, MaintenanceFilter, ClaimFilter
from silant.models import Machine, Maintenance, Claim


class Index(ListView):
    model = Machine
    template_name = 'index.html'
    context_object_name = 'machine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['machine_filter'] = MachineFilter(
                self.request.GET, queryset=Machine.objects.all())
            context['maintenance_filter'] = MaintenanceFilter(
                self.request.GET, queryset=Maintenance.objects.all())
            context['claim_filter'] = ClaimFilter(
                self.request.GET, queryset=Claim.objects.all())
            return context
        else:
            context['guest_filter'] = GuestFilter(self.request.GET, queryset=self.get_queryset())
        return context
