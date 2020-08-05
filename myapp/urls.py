from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    path('creating/', views.CreatingView.as_view(), name='creating'),
]
