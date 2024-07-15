from django.urls import path
from users.views import *
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('registration/',registration,name='registration'),
    path('login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
]