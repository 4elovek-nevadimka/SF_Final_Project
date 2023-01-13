from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from silant.filters import GuestFilter, MachineFilter, MaintenanceFilter, ClaimFilter
from silant.forms import MaintenanceForm, ClaimForm, MachineForm
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
    template_name = 'machine/machine_detail.html'
    context_object_name = 'machine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['machine_maintenances'] = Maintenance.objects.filter(machine=self.kwargs.get('pk'))
        context['machine_claims'] = Claim.objects.filter(machine=self.kwargs.get('pk'))
        return context


# CreateView для основных моделей
class MachineCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('silant.add_machine',)
    template_name = 'model_create.html'
    form_class = MachineForm

    def form_valid(self, form):
        form.instance.client = get_user_model().objects.get(id=self.request.user.id)
        return super(MachineCreateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('index')


class MaintenanceCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('silant.add_maintenance',)
    template_name = 'model_create.html'
    form_class = MaintenanceForm

    def get_success_url(self, **kwargs):
        return reverse('index')


class ClaimCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('silant.add_claim',)
    template_name = 'model_create.html'
    form_class = ClaimForm

    def get_success_url(self, **kwargs):
        return reverse('index')


# List / Create / Update / Delete Views для справочников
class LookupsListView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    permission_required = ('silant.view_vehicle_model', 'silant.view_engine_model', 'silant.view_transmission_model',
                           'silant.view_drive_axle_model', 'silant.view_steering_bridge_model',
                           'silant.view_maintenance_type',
                           'silant.view_failure_node', 'silant.view_recovery_method')
    template_name = 'lookups/lookups_list.html'
