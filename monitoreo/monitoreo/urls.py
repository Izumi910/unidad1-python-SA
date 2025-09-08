"""
URL configuration for monitoreo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dispositivos.views import inicio, panel_dispositivos, dispositivoVista, crear_dispositivo, editar_dispositivo, eliminar_dispositivo  # 👈 importa también panel_dispositivos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),                      # http://127.0.0.1:8000/
    path('panel/', panel_dispositivos, name="panel"),     # http://127.0.0.1:8000/panel/
    path('dispositivos/', inicio, name="dispositivos"), # http://127.0.0.1:8000/dispositivos/
    path('dispositivos/editar/<int:dispositivo_id>/', editar_dispositivo, name="editar_dispositivo"), # http://127.0.0.1:8000/dispositivos/editar/1/
    path('dispositivos/eliminar/<int:dispositivo_id>/', eliminar_dispositivo, name="eliminar_dispositivo"), # http://127.0.0.1:8000/dispositivos/eliminar/1/
    path('dispositivos/crear/', crear_dispositivo, name="crear_dispositivo"), # http://127.0.0.1:8000/dispositivos/crear/
    path('dispositivos/<int:dispositivo_id>/', dispositivoVista, name="dispositivo"), # http://127.0.0.1:8000/dispositivos/1/
]
