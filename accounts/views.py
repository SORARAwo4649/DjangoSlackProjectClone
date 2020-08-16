import json

from django.contrib.auth import login
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('myapp:creating')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # self.object に save() されたユーザーオブジェクトが格納される
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid
