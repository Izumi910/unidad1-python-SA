from django.contrib import admin

# Register your models here.
from .models import dispositivo


@admin.register(dispositivo)
class dispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre','consumo', 'estado')
    list_filter = ('estado',)
    search_fields = ('nombre',)