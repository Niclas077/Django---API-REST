from django.db import models

# Create your models here.

class Vehiculos(models.Model):
    marca = models.CharField(max_length=50)
    anyo = models.PositiveIntegerField()
    color = models.CharField(max_length=10)
    
    def visualizacion(self):
        return "{},{},{}".format(self.marca,self.anyo,self.color)
    
    def __str__(self):
        return self.visualizacion()
