from django.test import TestCase
from . import views
from rest_framework.test import APITestCase
from .models import Censo
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
import json


class CensoTests(APITestCase):
    def test_delete_censo_positive(self):
        c1 = Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11',
                                  nombre='Censocreate',
                                  fecha_fin='2018-12-15 11:11:11')

        self.assertEquals(Censo.objects.filter(nombre='Censocreate').exists(), True)

        Censo.objects.filter(id=c1.id).delete()
        self.assertEquals(Censo.objects.filter(nombre='Censocreate').exists(), False)
        return Censo.objects.filter(nombre='Censocreate').exists() is True


    def test_delete_censo_negative(self):
        censo = Censo.objects.create(id_votacion=200, rol='ASISTENTE', nombre='', fecha_ini='2017-11-15 11:11:11',
                                     fecha_fin='2018-12-15 11:11:11')
        censo.save()

        self.assertEquals(Censo.objects.filter(id=censo.id).exists(),True)
        Censo.objects.filter(id=censo.id, nombre='nombre_que_no_existe').delete()
        self.assertEquals(Censo.objects.filter(id=censo.id).exists(),True)

        return Censo.objects.filter(id=censo.id).exists() is True




    def test_filter_(self):
        c1 = Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11',
                                  nombre='Censocreate',
                                  fecha_fin='2018-12-15 11:11:11')
        return Censo.objects.filter(nombre='Censocreate').exists() is True

    def test_filter_Negative(self):
        c1 = Censo.objects.create(id_votacion=196, rol='PONENTE', fecha_ini='2017-11-15 11:11:11', nombre='Censocreate',
                                  fecha_fin='2018-12-15 11:11:11')
        return Censo.objects.filter(nombre='paco', id_votacion=196).exists() is False

    def test_update_censo(self):
        c1 = Censo.objects.create(id_votacion=196, rol='PONENTE', nombre="Censocreate", fecha_ini="2017-12-15 11:11:11",
                                  fecha_fin="2019-12-15 11:11:11")
        Censo.objects.update(id=196, nombre="CensoUpdate")
        Censo.objects.get(nombre="CensoUpdate")

    def test_update_censo_group(self):
        c1 = Censo.objects.create(id_votacion=196, rol='ASISTENTE', nombre="Censocreate",
                                  fecha_ini="2017-12-15 11:11:11",
                                  fecha_fin="2019-12-15 11:11:11")
        Censo.objects.update(id=196, nombre="CensoUpdate", rol='AMBOS')
        return Censo.objects.filter(nombre="CensoUpdate").exists()
