from django.shortcuts import render
from django.views.generic import ListView

from silant.models import Machine


class Index(ListView):
    model = Machine
    template_name = 'index.html'
    context_object_name = 'machine'
