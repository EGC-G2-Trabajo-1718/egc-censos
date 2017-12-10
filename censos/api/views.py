from .models import Censo
from .models import CensoDelete
from .serializers import CensoSerializer
from .serializers import DeleteSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


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


@api_view(['delete'])
def delete_censo(request):
    id = request.GET.get('id', '')
    try:
        user = Censo.objects.get(id=id)
        Censo.objects.delete(id=id)
    except Censo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    context = {'request': request}
    exito = CensoDelete.exito = True
    mensaje = CensoDelete.mensaje = "Eliminado con exito"

    serializer = DeleteSerializer(exito, mensaje)
    return Response(serializer.data)
