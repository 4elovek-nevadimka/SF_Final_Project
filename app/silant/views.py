from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from silant.filters import GuestFilter, MachineFilter, MaintenanceFilter, ClaimFilter
from silant.models import Machine, Maintenance, Claim


class Index(ListView):
    model = Machine
    template_name = 'index.html'
    context_object_name = 'machine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if self.request.user.is_authenticated:
                if self.request.user.role == 'MN':
                    context['machine_filter'] = MachineFilter(
                        self.request.GET, queryset=Machine.objects.all())
                    context['maintenance_filter'] = MaintenanceFilter(
                        self.request.GET, queryset=Maintenance.objects.all())
                    context['claim_filter'] = ClaimFilter(
                        self.request.GET, queryset=Claim.objects.all())
                elif self.request.user.role == 'CL':
                    context['machine_filter'] = MachineFilter(
                        self.request.GET, queryset=Machine.objects.filter(client=self.request.user))
                    context['maintenance_filter'] = MaintenanceFilter(
                        self.request.GET, queryset=Maintenance.objects.filter(machine__client=self.request.user))
                    context['claim_filter'] = ClaimFilter(
                        self.request.GET, queryset=Claim.objects.filter(machine__client=self.request.user))
                elif self.request.user.role == 'SC':
                    context['machine_filter'] = MachineFilter(
                        self.request.GET, queryset=Machine.objects.filter(service_company=self.request.user))
                    context['maintenance_filter'] = MaintenanceFilter(
                        self.request.GET, queryset=Maintenance.objects.filter(service_company=self.request.user))
                    context['claim_filter'] = ClaimFilter(
                        self.request.GET, queryset=Claim.objects.filter(machine__service_company=self.request.user))
            return context
        else:
            context['guest_filter'] = GuestFilter(self.request.GET, queryset=self.get_queryset())
        return context


class MachineDetail(LoginRequiredMixin, DetailView):
    model = Machine
    template_name = 'machine_detail.html'
    context_object_name = 'machine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['machine_maintenances'] = Maintenance.objects.filter(machine=self.kwargs.get('pk'))
        context['machine_claims'] = Claim.objects.filter(machine=self.kwargs.get('pk'))
        return context
