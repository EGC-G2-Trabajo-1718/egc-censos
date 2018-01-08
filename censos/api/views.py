from django.http import HttpResponse

from .models import Censo
from .serializers import CensoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json


@api_view(['GET'])
def get_censo(request):
    id = request.GET.get('id', '')
    try:
        user = Censo.objects.get(id=id)
    except Censo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    context = {'request': request}
    serializer = CensoSerializer(user, context=context)
    return Response(serializer.data)


def filter_censos(request):
    return None


def can_vote(request):
    return None


def create_censo(request):
    return None


def update_censo(request):
    return None


@api_view(['GET'])
def delete_censo(request):
    idRespuesta = request.GET.get('id', '')

    if idRespuesta and Censo.objects.filter(id=idRespuesta).exists():
        try:
            Censo.objects.filter(id=idRespuesta).delete()

        except Exception as e:
            response_data = {'Exito': False, 'Mensaje': 'No se ha podido eliminar'}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        response_data = {'Exito': True, 'Mensaje': 'Eliminado con exito'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        response_data = {'Exito': False, 'Mensaje': 'No se ha podido eliminar'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")



