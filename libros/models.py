from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.ManyToManyField(Autor)
    descripcion = models.TextField()
    fecha_pub = models.DateField()
    cant_pags = models.IntegerField()
    

    