from django.db import models

class Archivo(models.Model):
    idDocumento = models.IntegerField()
    nombre = models.CharField(max_length=50)
    archivo = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.nombre