from .models import Censo
from .serializers import CensoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime

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
    Censo.object.create(id_votacion='33',id_grupo='21',nombre='prueba',fecha_ini=datetime.now(),fecha_fin='')
    return None


@api_view(['GET'])
def update_censo(request):
    id = request.GET.get('id', '')
    nombre=request.GET.get('nombre', '')
    print(id, nombre)
    # fechaini = request.GET.get('fecha_ini', '')
    # if not fechaini:
    #     fechaini = datetime.now().strftime('%d/%m/%a')
    # fechafin = request.GET.get('fecha_fin', '')
    censo = None
    if id and Censo.objects.filter(id=id).exists():
        try:
             Censo.objects.filter(id=id).update(nombre=nombre)
             censo = Censo.objects.get(id=id)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_404_NOT_FOUND)
    context = {'request': request}
    serializer = CensoSerializer(censo, context=context)
    return Response(serializer.data)


def delete_censo(request):
    return None

