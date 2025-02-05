from django.db import models

# Create your models here.

from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/')
    enlace = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

