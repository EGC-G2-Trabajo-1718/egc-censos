from .models import Censo
from rest_framework import serializers


class CensoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Censo
        fields = ('id_votacion', 'id_grupo', 'nombre', 'fecha_ini', 'fecha_fin')

