from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View

from .forms import NameForm


class CreatingView(TemplateView):
    template_name = 'creating.html'
    success_url = reverse_lazy('myapp:creating')
    form_class = NameForm

    def get(self, request, *args, **kwargs):
        context = {
            'message': "操作して下さい",
        }
        return render(request, 'creating.html', context)

    def post(self, request, *args, **kwargs):
        context = {
            'name': request.POST['name']
        }
        names = request.POST['name']
        return render(request, 'creating_done.html', context)
