from django.db import models

# Create your models here.
class Asignaturas(models.Model):
    NDI=models.CharField(primary_key=True, max_length=10)
    Nombre=models.CharField(max_length=40)
    Horas_t=models.PositiveSmallIntegerField()
    Horas_p=models.PositiveSmallIntegerField()
    Creditos=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.Nombre