from django.db import models

# Create your models here.
class dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    consumo = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    

