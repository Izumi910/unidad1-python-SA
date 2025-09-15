from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', views.registro_empresa, name='registro_empresa'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dispositivos/', views.listar_dispositivos, name='listar_dispositivos'),
    path('dispositivo/<int:id>/', views.detalle_dispositivo, name='detalle_dispositivo'),
    path('mediciones/', views.listar_mediciones, name='listar_mediciones'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]