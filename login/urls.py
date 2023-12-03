
from django.urls import path
from django.contrib.auth import views as auth_views
from login import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),# hacemos el llamado a la vista de django LoginViews que nos permite ejecutar de mejor manera el inicio de sesion
   # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]