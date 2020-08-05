from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', views.PasswordChangeView.as_view(),
         name='password_change'),
    path('accounts/password_change/done/',
         views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/', views.PasswordResetView.as_view(),
         name='password_reset'),
    path('accounts/password_reset/done/', views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('accounts/reset/done/', views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
