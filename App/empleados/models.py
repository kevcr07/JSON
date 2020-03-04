from django.db import models

#se crea un modelo llamado usuario, en el cual creara los campos tanto dentro de la base de datos como en la API
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    edad = models.IntegerField()
    creacion = models.DateField(auto_now_add=True)
    editado = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre




