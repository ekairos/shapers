from django.urls import path
from . import views
from allauth.account.views import PasswordChangeView

urlpatterns = [
    path('', views.profile, name='profile'),
    path('password-change/',
         PasswordChangeView.as_view(
             success_url='/profile/',
             template_name='allauth/account/password_change.html'),
         name='profile_password_change')
]
