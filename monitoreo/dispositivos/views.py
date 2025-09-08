from django.shortcuts import get_object_or_404, render, redirect
from .forms import DispositivoForm
# Create your views here.
from .models import dispositivo

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

def inicio(request):
    d = dispositivo.objects.all()
    return render(request, "dispositivos/inicio.html", {"dispositivo": d})

def dispositivoVista(request, dispositivo_id):
    d = dispositivo.objects.get(id=dispositivo_id)

    return render(request, "dispositivos/dispositivo.html", {"dispositivo": d})

def disposivo(request, dispositivo_id):
    d = dispositivo.objects.get(id=dispositivo_id)
    if request.method == "POST":
        form = DispositivoForm(request.POST, instance=d)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = DispositivoForm(instance=d)
    return render(request, "dispositivos/editar.html", {"form": form})

def crear_dispositivo(request):
    if request.method == "POST":
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = DispositivoForm()
    return render(request, "dispositivos/crear.html", {"form": form})

def editar_dispositivo(request, dispositivo_id):
    d = get_object_or_404(dispositivo, id=dispositivo_id)
    if request.method == "POST":
        form = DispositivoForm(request.POST, instance=d)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = DispositivoForm(instance=d)
    return render(request, "dispositivos/editar.html", {"form": form})

def eliminar_dispositivo(request, dispositivo_id):
    d = get_object_or_404(dispositivo, id=dispositivo_id)
    if request.method == "POST":
        d.delete()
        return redirect("inicio")
    return render(request, "dispositivos/eliminar.html", {"dispositivo": d})










