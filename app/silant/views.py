from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

from silant.filters import GuestFilter, MachineFilter, MaintenanceFilter, ClaimFilter
from silant.forms import MaintenanceForm, ClaimForm, MachineForm, VehicleModelForm, EngineModelForm, \
    TransmissionModelForm, DriveAxleModelForm, SteeringBridgeModelForm, MaintenanceTypeForm, FailureNodeForm, \
    RecoveryMethodForm
from silant.models import Machine, Maintenance, Claim, VehicleModel, EngineModel, TransmissionModel, DriveAxleModel, \
    SteeringBridgeModel, MaintenanceType, FailureNode, RecoveryMethod


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


class LookupVehicleModelDetailView(DetailView):
    model = VehicleModel
    template_name = 'lookups/lookup_detail.html'
    context_object_name = 'lookup_model'


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


class LookupEngineModelListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('silant.view_enginemodel',)
    model = EngineModel
    template_name = 'lookups/lookup_list.html'
    context_object_name = 'lookup_table_values'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lookup_table_name'] = 'Модели двигателей'
        context['href_create'] = 'lookup_engine_model_create'
        context['href_update'] = 'lookup_engine_model_update'
        context['href_delete'] = 'lookup_engine_model_delete'
        return context


class LookupEngineModelDetailView(DetailView):
    model = EngineModel
    template_name = 'lookups/lookup_detail.html'
    context_object_name = 'lookup_model'


class LookupEngineModelCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('silant.add_enginemodel',)
    template_name = 'lookups/lookup_create.html'
    form_class = EngineModelForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_engine_model')


class LookupEngineModelUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('silant.change_enginemodel',)
    model = EngineModel
    template_name = 'lookups/lookup_update.html'
    form_class = EngineModelForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_engine_model')


class LookupEngineModelDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('silant.delete_enginemodel',)
    model = EngineModel
    template_name = 'lookups/lookup_delete.html'
    context_object_name = 'lookup_model'

    def get_success_url(self, **kwargs):
        return reverse('lookup_engine_model')


class LookupTransmissionModelListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('silant.view_transmissionmodel',)
    model = TransmissionModel
    template_name = 'lookups/lookup_list.html'
    context_object_name = 'lookup_table_values'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lookup_table_name'] = 'Модели трансмиссий'
        context['href_create'] = 'lookup_transmission_model_create'
        context['href_update'] = 'lookup_transmission_model_update'
        context['href_delete'] = 'lookup_transmission_model_delete'
        return context


class LookupTransmissionModelDetailView(DetailView):
    model = TransmissionModel
    template_name = 'lookups/lookup_detail.html'
    context_object_name = 'lookup_model'


class LookupTransmissionModelCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('silant.add_transmissionmodel',)
    template_name = 'lookups/lookup_create.html'
    form_class = TransmissionModelForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_transmission_model')


class LookupTransmissionModelUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('silant.change_transmissionmodel',)
    model = TransmissionModel
    template_name = 'lookups/lookup_update.html'
    form_class = TransmissionModelForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_transmission_model')


class LookupTransmissionModelDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('silant.delete_transmissionmodel',)
    model = TransmissionModel
    template_name = 'lookups/lookup_delete.html'
    context_object_name = 'lookup_model'

    def get_success_url(self, **kwargs):
        return reverse('lookup_transmission_model')


class LookupDriveAxleModelListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('silant.view_driveaxlemodel',)
    model = DriveAxleModel
    template_name = 'lookups/lookup_list.html'
    context_object_name = 'lookup_table_values'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lookup_table_name'] = 'Модели ведущих мостов'
        context['href_create'] = 'lookup_drive_axle_model_create'
        context['href_update'] = 'lookup_drive_axle_model_update'
        context['href_delete'] = 'lookup_drive_axle_model_delete'
        return context


class LookupDriveAxleModelDetailView(DetailView):
    model = DriveAxleModel
    template_name = 'lookups/lookup_detail.html'
    context_object_name = 'lookup_model'


class LookupDriveAxleModelCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('silant.add_driveaxlemodel',)
    template_name = 'lookups/lookup_create.html'
    form_class = DriveAxleModelForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_drive_axle_model')


class LookupDriveAxleModelUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('silant.change_driveaxlemodel',)
    model = DriveAxleModel
    template_name = 'lookups/lookup_update.html'
    form_class = DriveAxleModelForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_drive_axle_model')


class LookupDriveAxleModelDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('silant.delete_driveaxlemodel',)
    model = DriveAxleModel
    template_name = 'lookups/lookup_delete.html'
    context_object_name = 'lookup_model'

    def get_success_url(self, **kwargs):
        return reverse('lookup_drive_axle_model')


class LookupSteeringBridgeModelListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('silant.view_steeringbridgemodel',)
    model = SteeringBridgeModel
    template_name = 'lookups/lookup_list.html'
    context_object_name = 'lookup_table_values'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lookup_table_name'] = 'Модели управляемых мостов'
        context['href_create'] = 'lookup_steering_bridge_model_create'
        context['href_update'] = 'lookup_steering_bridge_model_update'
        context['href_delete'] = 'lookup_steering_bridge_model_delete'
        return context


class LookupSteeringBridgeModelDetailView(DetailView):
    model = SteeringBridgeModel
    template_name = 'lookups/lookup_detail.html'
    context_object_name = 'lookup_model'


class LookupSteeringBridgeModelCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('silant.add_steeringbridgemodel',)
    template_name = 'lookups/lookup_create.html'
    form_class = SteeringBridgeModelForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_steering_bridge_model')


class LookupSteeringBridgeModelUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('silant.change_steeringbridgemodel',)
    model = SteeringBridgeModel
    template_name = 'lookups/lookup_update.html'
    form_class = SteeringBridgeModelForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_steering_bridge_model')


class LookupSteeringBridgeModelDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('silant.delete_steeringbridgemodel',)
    model = SteeringBridgeModel
    template_name = 'lookups/lookup_delete.html'
    context_object_name = 'lookup_model'

    def get_success_url(self, **kwargs):
        return reverse('lookup_steering_bridge_model')


class LookupMaintenanceTypeListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('silant.view_maintenancetype',)
    model = MaintenanceType
    template_name = 'lookups/lookup_list.html'
    context_object_name = 'lookup_table_values'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lookup_table_name'] = 'Виды ТО'
        context['href_create'] = 'lookup_maintenance_type_create'
        context['href_update'] = 'lookup_maintenance_type_update'
        context['href_delete'] = 'lookup_maintenance_type_delete'
        return context


class LookupMaintenanceTypeDetailView(DetailView):
    model = MaintenanceType
    template_name = 'lookups/lookup_detail.html'
    context_object_name = 'lookup_model'


class LookupMaintenanceTypeCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('silant.add_maintenancetype',)
    template_name = 'lookups/lookup_create.html'
    form_class = MaintenanceTypeForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_maintenance_type')


class LookupMaintenanceTypeUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('silant.change_maintenancetype',)
    model = MaintenanceType
    template_name = 'lookups/lookup_update.html'
    form_class = MaintenanceTypeForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_maintenance_type')


class LookupMaintenanceTypeDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('silant.delete_maintenancetype',)
    model = MaintenanceType
    template_name = 'lookups/lookup_delete.html'
    context_object_name = 'lookup_model'

    def get_success_url(self, **kwargs):
        return reverse('lookup_maintenance_type')


class LookupFailureNodeListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('silant.view_failurenode',)
    model = FailureNode
    template_name = 'lookups/lookup_list.html'
    context_object_name = 'lookup_table_values'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lookup_table_name'] = 'Узлы отказа'
        context['href_create'] = 'lookup_failure_node_create'
        context['href_update'] = 'lookup_failure_node_update'
        context['href_delete'] = 'lookup_failure_node_delete'
        return context


class LookupFailureNodeDetailView(DetailView):
    model = FailureNode
    template_name = 'lookups/lookup_detail.html'
    context_object_name = 'lookup_model'


class LookupFailureNodeCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('silant.add_failurenode',)
    template_name = 'lookups/lookup_create.html'
    form_class = FailureNodeForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_failure_node')


class LookupFailureNodeUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('silant.change_failurenode',)
    model = FailureNode
    template_name = 'lookups/lookup_update.html'
    form_class = FailureNodeForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_failure_node')


class LookupFailureNodeDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('silant.delete_failurenode',)
    model = FailureNode
    template_name = 'lookups/lookup_delete.html'
    context_object_name = 'lookup_model'

    def get_success_url(self, **kwargs):
        return reverse('lookup_failure_node')


class LookupRecoveryMethodListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('silant.view_recoverymethod',)
    model = RecoveryMethod
    template_name = 'lookups/lookup_list.html'
    context_object_name = 'lookup_table_values'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lookup_table_name'] = 'Способы восстановления'
        context['href_create'] = 'lookup_recovery_method_create'
        context['href_update'] = 'lookup_recovery_method_update'
        context['href_delete'] = 'lookup_recovery_method_delete'
        return context


class LookupRecoveryMethodDetailView(DetailView):
    model = RecoveryMethod
    template_name = 'lookups/lookup_detail.html'
    context_object_name = 'lookup_model'


class LookupRecoveryMethodCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('silant.add_recoverymethod',)
    template_name = 'lookups/lookup_create.html'
    form_class = RecoveryMethodForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_recovery_method')


class LookupRecoveryMethodUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('silant.change_recoverymethod',)
    model = RecoveryMethod
    template_name = 'lookups/lookup_update.html'
    form_class = RecoveryMethodForm

    def get_success_url(self, **kwargs):
        return reverse('lookup_recovery_method')


class LookupRecoveryMethodDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('silant.delete_recoverymethod',)
    model = RecoveryMethod
    template_name = 'lookups/lookup_delete.html'
    context_object_name = 'lookup_model'

    def get_success_url(self, **kwargs):
        return reverse('lookup_recovery_method')
