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


@api_view(['filter'])
def filter_censos(request):
    nombre = request.GET.get('nombre', '')
    fecha_ini = request.GET.get('fecha_ini', '')
    fecha_fin = request.GET.get('fecha_fin', '')
    id_votacion = request.GET.get('id_votacion', '')
    id_grupo = request.GET.get('id_grupo', '')
    try:
        user = Censo.objects.filter(nombre=nombre, fecha_fin=fecha_fin, fecha_ini=fecha_ini, id_votacion=id_votacion, id_grupo=id_grupo)
    except Censo.doesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    context = {'request': request}
    serializer = CensoSerializer(user, context=context)
    return Response(serializer.data)


def can_vote(request):
    return None


def create_censo(request):
    return None


def update_censo(request):
    return None


def delete_censo(request):
    return None

