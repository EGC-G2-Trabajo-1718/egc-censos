from django.test import TestCase
from . import views
from rest_framework.test import APITestCase
from .models import Censo
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
import json


class CensoTests(APITestCase):
    def test_delete_censo_positiv0_0(self):
        c1 = Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11',
                                  nombre='Censocreate',
                                  fecha_fin='2018-12-15 11:11:11')

        self.assertEquals(Censo.objects.filter(nombre='Censocreate').exists(), True)
        Censo.objects.filter(id=c1.id).delete()
        self.assertEquals(Censo.objects.filter(nombre='Censocreate').exists(), False)

    def test_delete_censo_negativo_0(self):
        excepcion = False
        censo = Censo.objects.create(id_votacion=200, rol='ASISTENTE', nombre='', fecha_ini='2017-11-15 11:11:11',
                                     fecha_fin='2018-12-15 11:11:11')

        try:
            Censo.objects.filter(id='').delete()
        except:
            excepcion = True

        self.assertEquals(excepcion, True)

    def test_delete_censo_positivo_1(self):
        c2 = Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11',
                                  nombre='Censocreate1',
                                  fecha_fin='2018-12-15 11:11:11')
        c3 = Censo.objects.create(id_votacion=201, rol='ASISTENTE', fecha_ini='2017-10-01 09:09:09',
                                  nombre='Censocreate2', fecha_fin='2018-05-05 05:05:05')

        conjunto = Censo.objects.all()
        self.assertEquals(conjunto.count(), 2)
        Censo.objects.filter(id=c2.id).delete()
        conjunto1 = Censo.objects.all()
        self.assertEquals(conjunto1.count(), 1)
        Censo.objects.filter(id=c3.id).delete()
        conjunto2 = Censo.objects.all()
        self.assertEquals(conjunto2.count(), 0)

    def test_delete_censo_negativo_1(self):

        censo1 = Censo.objects.create(id_votacion=200, rol='ASISTENTE', nombre='', fecha_ini='2017-11-15 11:11:11',
                                     fecha_fin='2018-12-15 11:11:11')

        conjunto = Censo.objects.all()
        self.assertEquals(conjunto.count(), 1)
        Censo.objects.filter(id=35252).delete()
        conjunto1 = Censo.objects.all()
        self.assertEquals(conjunto.count(), 1)




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
