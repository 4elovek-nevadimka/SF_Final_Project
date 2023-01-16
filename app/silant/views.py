from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

from silant.filters import GuestFilter, MachineFilter, MaintenanceFilter, ClaimFilter
from silant.forms import MaintenanceForm, ClaimForm, MachineForm, VehicleModelForm
from silant.models import Machine, Maintenance, Claim, VehicleModel


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
    permission_required = ('silant.view_vehiclemodel', 'silant.view_enginemodel', 'silant.view_transmissionmodel',
                           'silant.view_driveaxlemodel', 'silant.view_steeringbridgemodel',
                           'silant.view_maintenancetype',
                           'silant.view_failurenode', 'silant.view_recoverymethod')
    template_name = 'lookups/lookups_list.html'


class LookupVehicleModelListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('silant.view_vehiclemodel',)
    model = VehicleModel
    template_name = 'lookups/lookup_list.html'
    context_object_name = 'lookup_table_values'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lookup_table_name'] = 'Модели техники'
        # context['href_create'] = reverse('index')
        context['href_create'] = 'lookup_vehicle_model_create'
        context['href_update'] = 'lookup_vehicle_model_update'
        context['href_delete'] = 'lookup_vehicle_model_delete'
        return context


class LookupVehicleModelCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('silant.add_vehiclemodel',)
    template_name = 'lookups/lookup_create.html'
    form_class = VehicleModelForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_vehicle_model')


class LookupVehicleModelUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('silant.change_vehiclemodel',)
    model = VehicleModel
    template_name = 'lookups/lookup_update.html'
    form_class = VehicleModelForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_vehicle_model')


class LookupVehicleModelDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('silant.delete_vehiclemodel',)
    model = VehicleModel
    template_name = 'lookups/lookup_delete.html'
    context_object_name = 'lookup_model'

    def get_success_url(self, **kwargs):
        return reverse('lookup_vehicle_model')
