from django.shortcuts import render
# Create your views here.

def panel_dispositivos(request):
    dispositivos = [
        {"nombre": "Sensor Temperatura", "consumo": 50},
        {"nombre": "Medidor Solar", "consumo": 120},
        {"nombre": "Sensor Movimiento", "consumo": 30},
        {"nombre": "Calefactor", "consumo": 200},
    ]

    consumo_maximo = 100 

    return render(request, "dispositivos/panel.html", {
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo
    })

from .models import dispositivo
def inicio(request):
    d = dispositivo.objects.all()
    return render(request, "dispositivos/inicio.html", {"dispositivo": d})


def dispositivoVista(request, dispositivo_id):
    d = dispositivo.objects.get(id=dispositivo_id)

    return render(request, "dispositivos/dispositivo.html", {"dispositivo": d})