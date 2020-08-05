from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class CreatingView(TemplateView):
    template_name = 'creating.html'
    success_url = reverse_lazy('myapp:creating')
