from django.test import TestCase
from .models import Censo
from rest_framework.test import APITestCase
from . import views

class CensoTests(APITestCase):

    def test_delete_censo(self):
        c1 = Censo.objects.create(id_votacion=196, id_grupo=101, nombre="Censocreate", fecha_ini="2017-12-15 11:11:11",
                                  fecha_fin="2018-12-15 11:11:11")
        c2 = Censo.objects.get(nombre="Censocreate")
        Censo.objects.filter(nombre="Censocreate").delete()

    def test_update_censo(self):
        c1 = Censo.objects.create(id_votacion=196, id_grupo=101, nombre="Censocreate", fecha_ini="2017-12-15 11:11:11",
                                  fecha_fin="2019-12-15 11:11:11")
        Censo.objects.update(id=196, nombre="CensoUpdate")
        Censo.objects.get(nombre="CensoUpdate")

    def test_update_censo_group(self):
        c1 = Censo.objects.create(id_votacion=196, id_grupo=101, nombre="Censocreate",
                                  fecha_ini="2017-12-15 11:11:11",
                                  fecha_fin="2019-12-15 11:11:11")
        Censo.objects.update(id=196, nombre="CensoUpdate",id_grupo=103)
        Censo.objects.get(nombre="CensoUpdate")

