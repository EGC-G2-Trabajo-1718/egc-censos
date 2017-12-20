from .models import Censo
from .serializers import CensoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime


@api_view(['GET'])
def get_censo(request):
    id = request.GET.get('id', '')

    if id and Censo.objects.filter(id=id).exists():
        try:
            censo = Censo.objects.get(id=id)
        except Censo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    context = {'request': request}
    serializer = CensoSerializer(censo, context=context)
    return Response(serializer.data)


def filter_censos(request):
    return None


def can_vote(request):
    return None


@api_view(['GET'])
def create_censo(request):
    id_grupo = request.GET.get('id_grupo', '')
    id_votacion = request.GET.get('id_votacion', '')
    nombre = request.GET.get('nombre', '')
    fecha_ini = request.GET.get('fecha_ini', '')
    fecha_fin = request.GET.get('fecha_fin', '')

    if not nombre:
        nombre = 'Censo de ' + id_votacion + ' para el grupo ' + id_grupo

    if not fecha_ini:
        fecha_ini = datetime.now()

    if not fecha_fin:
        fecha_fin = datetime.now()
        # TODO pedir fecha de fin a la api de adminsitración de votos

    print(id_grupo, id_votacion)
    if id_grupo and id_votacion:
        try:
            censo = Censo.objects.create(id_votacion=id_votacion, id_grupo=id_grupo, nombre=nombre, fecha_ini=fecha_ini, fecha_fin=fecha_fin)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    context = {'request': request}
    serializer = CensoSerializer(censo, context=context)
    return Response(serializer.data)


@api_view(['GET'])
def update_censo(request):
    id = request.GET.get('id', '')
    nombre = request.GET.get('nombre', Censo.objects.get(id=id).nombre)
    idgrupo = request.GET.get('id_grupo', Censo.objects.get(id=id).id_grupo)
    idvotacion = request.GET.get('id_votacion', Censo.objects.get(id=id).id_votacion)
    print(id, nombre)
    fechaini = request.GET.get('fecha_ini', '')
    if not fechaini:
        fechaini = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fechafin = request.GET.get('fecha_fin', Censo.objects.get(id=id).fecha_fin)
    censo = None
    if id and Censo.objects.filter(id=id).exists():
        try:
            Censo.objects.filter(id=id).update(nombre=nombre, fecha_ini=fechaini, fecha_fin=fechafin, id_grupo=idgrupo,
                                               id_votacion=idvotacion)
            censo = Censo.objects.get(id=id)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_404_NOT_FOUND)
    context = {'request': request}
    serializer = CensoSerializer(censo, context=context)
    return Response(serializer.data)


def delete_censo(request):
    return None
