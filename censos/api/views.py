from .models import Censo
from .serializers import CensoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_censo(request):
    id = request.GET.get('id', '')
    try:
        censo = Censo.objects.get(id=id)
    except Censo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    context = {'request': request}
    serializer = CensoSerializer(censo, context=context)
    return Response(serializer.data)


@api_view(['GET'])
def filter_censos(request):
    nombre = request.GET.get('nombre', '')
    fecha_ini = request.GET.get('fecha_ini', '')
    fecha_fin = request.GET.get('fecha_fin', '')
    id_votacion = request.GET.get('id_votacion', '')
    id_grupo = request.GET.get('id_grupo', '')

    try:
        if nombre and fecha_ini and fecha_fin and id_votacion and id_grupo:
            censos = Censo.objects.filter(nombre=nombre, fecha_fin=fecha_fin, fecha_ini=fecha_ini, id_votacion=id_votacion, id_grupo=id_grupo)
        """elif nombre and not fecha_ini and not fecha_fin and not id_votacion and not id_grupo:
            censos = Censo.objects.filter(nombre=nombre)
        elif nombre and fecha_ini and not fecha_fin and not id_votacion and not id_grupo:
            censos = Censo.objects.filter(nombre=nombre, fecha_ini=fecha_ini)
        elif nombre and fecha_ini and fecha_fin and not id_votacion and not id_grupo:
            censos = Censo.objects.filter(nombre=nombre, fecha_ini=fecha_ini, fecha_fin=fecha_fin)
        elif nombre and fecha_ini and fecha_fin and id_votacion and not id_grupo:
            censos = Censo.objects.filter(nombre=nombre, fecha_ini=fecha_ini, fecha_fin=fecha_fin, id_votacion=id_votacion)
        elif not nombre and fecha_ini and fecha_fin and id_votacion and  id_grupo:
            censos = Censo.objects.filter(fecha_ini=fecha_ini, fecha_fin=fecha_fin, id_votacion=id_votacion, id_grupo=grupo)
        elif not nombre and not fecha_ini and fecha_fin and id_votacion and id_grupo:
            censos = Censo.objects.filter(fecha_fin=fecha_fin, id_votacion=id_votacion, id_grupo=grupo)
        elif not nombre and not fecha_ini and not fecha_fin"""
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    context = {'request': request}
    serializer = CensoSerializer(censos, context=context, many=True)
    return Response(serializer.data)


def can_vote(request):
    return None


def create_censo(request):

    return None


def update_censo(request):
    return None


def delete_censo(request):
    return None

