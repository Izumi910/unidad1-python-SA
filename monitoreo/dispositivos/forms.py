from django import forms
from .models import dispositivo

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = dispositivo
        fields = ['nombre', 'consumo', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'consumo': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError("Este campo debe tener al menos 3 caracteres.")
        return nombre
