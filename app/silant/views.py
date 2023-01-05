from django.views.generic import ListView

from silant.filters import MachineFilter
from silant.models import Machine


class Index(ListView):
    model = Machine
    template_name = 'index.html'
    context_object_name = 'machine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            pass
        else:
            context['machine_filter'] = MachineFilter(self.request.GET, queryset=self.get_queryset())
        return context
