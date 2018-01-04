from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Censo(models.Model):
    id_votacion = models.IntegerField(blank=False, null=False)
    id_grupo = models.IntegerField(blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    fecha_ini = models.DateTimeField(default=timezone.now, blank=True, null=False)
    fecha_fin = models.DateTimeField(blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'censo'



