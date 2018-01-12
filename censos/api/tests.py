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

    def test_filter_(self):
        c1 = Censo.objects.create(id_votacion=196, rol='ASISTENTE', fecha_ini='2017-11-15 11:11:11',
                                  nombre='Censocreate', fecha_fin='2018-12-15 11:11:11')
        return Censo.objects.filter(nombre='Censocreate').exists() is True

    def test_filter_Negative(self):
        c1 = Censo.objects.create(id_votacion=196, rol='PONENTE', fecha_ini='2017-11-15 11:11:11', nombre='Censocreate',
                                  fecha_fin='2018-12-15 11:11:11')
        return Censo.objects.filter(nombre='paco', id_votacion=196).exists() is False

    def test_filter(self):
        c1 = Censo.objects.create(id_votacion=4, rol='PONENTE', fecha_ini='2017-11-15 11:11:11', nombre='Censocreate',
                                  fecha_fin='2018-12-15 11:11:11')
        return Censo.objects.filter(id_votacion=4).exists() is True

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