from django.test import TestCase
from . import views
from rest_framework.test import APITestCase
from .models import Censo


class CensoTests(APITestCase):
    def test_delete_censo(self):
        c1 = Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11',
                                  nombre='Censocreate',
                                  fecha_fin='2018-12-15 11:11:11')
        c1.save()
        c2 = Censo.objects.all()
        self.assertEquals(c2.count(), 1)
        Censo.objects.filter(id=c1.id).delete()
        c3 = Censo.objects.all()
        self.assertEquals(c3.count(), 0)

    def test_filter(self):
        excepcion = False
        try:
            c2 = Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11',
                                 nombre='Censocreate', fecha_fin='2018-12-15 11:11:11')
            c1 = Censo.objects.filter(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11',
                                 nombre='Censocreate', fecha_fin='2018-12-15 11:11:11')
            self.assertIs(c1, c2)
        except:
            excepcion = True
        self.assertEquals(excepcion, True)

    def test_filter_(self):
        excepcion = False
        try:
            c2 = Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11',
                                 nombre='Censocreate', fecha_fin='2018-12-15 11:11:11')
            c1 = Censo.objects.filter(id_votacion=196, rol='ASISTENTE')
            self.assertIs(c1, c2)
        except:
            excepcion = True
        self.assertEquals(excepcion, True)

    def test_filter_fechas(self):
        excepcion = False
        try:
            c2 = Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11',
                                 nombre='Censocreate', fecha_fin='2018-12-15 11:11:11')
            c1 = Censo.objects.filter(fecha_ini='2017-11-15 11:11:11', fecha_fin='2018-12-15 11:11:11')
            self.assertIs(c1, c2)
        except:
            excepcion = True
        self.assertEquals(excepcion, True)

    def test_filter_Negative(self):
        excepcion = False
        try:
            Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11', nombre='Censocreate',fecha_fin='2018-12-15 11:11:11')
            c1 = Censo.objects.filter(id_votacion=1888)
            self.assertNotEquals(c1.count(), 0)
        except:
            excepcion = True
        self.assertEquals(excepcion, True)

    def test_filter_NegativeRol(self):
        excepcion = False
        try:
            Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11', nombre='Censocreate',fecha_fin='2018-12-15 11:11:11')
            c1 = Censo.objects.filter(rol='NONE')
            self.assertNotEquals(c1.count(), 0)
        except:
            excepcion = True
        self.assertEquals(excepcion, True)

    def test_filter_Negativefecha_ini(self):
        excepcion = False
        try:
            Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11', nombre='Censocreate',fecha_fin='2018-12-15 11:11:11')
            c1 = Censo.objects.filter(fecha_ini='2018-11-15 11:11:11')
            self.assertNotEquals(c1.count(), 0)
        except:
            excepcion = True
        self.assertEquals(excepcion, True)


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
