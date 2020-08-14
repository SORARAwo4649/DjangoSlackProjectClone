from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signup/ajax/', views.ValidatePasswordAjaxView.as_view(), name='ajax'),
]
