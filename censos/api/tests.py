from rest_framework.test import APITestCase
from .models import Censo
from rest_framework.response import Response
from rest_framework import status


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
            Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11',
                                 nombre='Censocreate', fecha_fin='2018-12-15 11:11:11')
            c1 = Censo.objects.filter(id_votacion=1888)
            self.assertNotEquals(c1.count(), 0)
        except:
            excepcion = True
        self.assertEquals(excepcion, True)

    def test_filter_NegativeRol(self):
        excepcion = False
        try:
            Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11',
                                 nombre='Censocreate', fecha_fin='2018-12-15 11:11:11')
            c1 = Censo.objects.filter(rol='NONE')
            self.assertNotEquals(c1.count(), 0)
        except:
            excepcion = True
        self.assertEquals(excepcion, True)

    def test_filter_Negativefecha_ini(self):
        excepcion = False
        try:
            Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11',
                                 nombre='Censocreate', fecha_fin='2018-12-15 11:11:11')
            c1 = Censo.objects.filter(fecha_ini='2018-11-15 11:11:11')
            self.assertNotEquals(c1.count(), 0)
        except:
            excepcion = True
        self.assertEquals(excepcion, True)

    def test_update_censo(self):
        Censo.objects.create(id_votacion=196, rol='PONENTE', nombre="Censocreate", fecha_ini="2017-12-15 11:11:11",
                             fecha_fin="2019-12-15 11:11:11")
        c2 = Censo.objects.get(id_votacion=196)
        Censo.objects.update(id_votacion=196, nombre="CensoUpdate")
        c1 = Censo.objects.get(nombre="CensoUpdate")
        self.assertEquals(c2, c1)

    def test_update_censo_rol(self):
        Censo.objects.create(id_votacion=196, rol='ASISTENTE', nombre="Censocreate",
                             fecha_ini="2017-12-15 11:11:11",
                             fecha_fin="2019-12-15 11:11:11")
        c1 = Censo.objects.get(id_votacion=196)
        Censo.objects.update(id_votacion=196, nombre="CensoUpdate", rol='AMBOS')
        c2 = Censo.objects.get(id_votacion=196)
        self.assertEquals(c2, c1)

    def test_update_censo_rolNEGATIVE(self):
        exception = False

        Censo.objects.create(id_votacion=196, rol='ASISTENTE', nombre="Censocreate",
                             fecha_ini="2017-12-15 11:11:11",
                             fecha_fin="2019-12-15 11:11:11")
        try:
            Censo.objects.update(id=196, rol='miroleselmejorporquesoybueno')
        except:
            exception = True
        self.assertEquals(exception, True)

    def test_update_censo_NoExiste(self):
        exception = False

        Censo.objects.create(id_votacion=196, rol='ASISTENTE', nombre="Censocreate",
                             fecha_ini="2017-12-15 11:11:11",
                             fecha_fin="2019-12-15 11:11:11")
        try:
            c1 = Censo.objects.update(id=19999)
            self.assertIsNone(c1)
        except:
            exception = True
        self.assertEquals(exception, True)

    def test_update_censo_modificafechafinNEGATIVO(self):
        exception = False

        Censo.objects.create(id_votacion=196, rol='ASISTENTE', nombre="Censocreate",
                             fecha_ini="2017-12-15 11:11:11",
                             fecha_fin="2019-12-15 11:11:11")
        try:
            Censo.objects.update(id=196, fecha_fin="2014/13/14")

        except:
            exception = True
        self.assertEquals(exception, True)

    def test_update_censo_modificafechainiNEGATIVO(self):
        exception = False

        Censo.objects.create(id_votacion=196, rol='ASISTENTE', nombre="Censocreate",
                             fecha_ini="2017-12-15 11:11:11",
                             fecha_fin="2019-12-15 11:11:11")
        try:
            Censo.objects.update(id=196, fecha_ini="2014/13/14")

        except:
            exception = True
        self.assertEquals(exception, True)

    def test_create_positive_0(self):
        c1 = Censo.objects.create(id_votacion=200, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11',
                                  nombre='Censocreate',
                                  fecha_fin='2018-12-15 11:11:11')
        self.assertEqual(Censo.objects.filter(id_votacion=200).exists(), True)

    def test_create_positive_1(self):
        c1 = Censo.objects.create(id_votacion=201, rol='PONENTE', fecha_ini='2018-11-20 11:11:11',
                                  nombre='Censocreate2',
                                  fecha_fin='2018-12-15 11:11:11')
        self.assertEqual(Censo.objects.filter(id_votacion=201).exists(), True)

    def test_create_negative_0(self):
        exception = False
        try:
            censo = Censo.objects.create(id_votacion=200, rol='ASISTENTE', nombre=None, fecha_ini='2017-11-15 11:11:11',
                                         fecha_fin='2018-12-15 11:11:11')
        except:
            exception = True

        self.assertEqual(exception, True)

    def test_create_negative_1(self):
        exception = False
        try:
            censo = Censo.objects.create(id_votacion=None, rol='ASISTENTE', nombre='CensoCreate3',
                                         fecha_ini='2017-11-15 11:11:11',
                                         fecha_fin='2018-12-15 11:11:11')
        except:
            exception = True

        self.assertEqual(exception, True)
