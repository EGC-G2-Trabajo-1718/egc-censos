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


def filter_censos(request):
    return None


def can_vote(request):
    return None


def create_censo(request):
    return None


def update_censo(request):
    id = request.GET.get('id')
    nombre=request.GET.get('nombre')
    fechafin = request.GET.get('fecha_fin')
    if id and Censo.obects.filter(id=id).exists():
       censo = Censo.objets.filter(id=id).update(nombre=nombre, fecha_ini=time.strftime('%X'), fecha_fin=fechafin)

    context = {'request': request}
    serializer = CensoSerializer(censo, context=context)
    return Response(serializer.data)


def delete_censo(request):
    return None

