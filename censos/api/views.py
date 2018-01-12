from django.http import HttpResponse
from .models import Censo
from .serializers import CensoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime
import json
import requests

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


@api_view(['GET'])
def filter_censos(request):
    nombre = request.GET.get('nombre', '')
    fecha_ini = request.GET.get('fecha_ini', '')
    fecha_fin = request.GET.get('fecha_fin', '')
    id_votacion = request.GET.get('id_votacion', '')
    rol = request.GET.get('rol', '')

    # TODO: Simplificar esto con filter(**args)
    try:
        if nombre and fecha_ini and fecha_fin and id_votacion and rol:
            censos = Censo.objects.filter(nombre=nombre, fecha_fin=fecha_fin, fecha_ini=fecha_ini,
                                          id_votacion=id_votacion, rol=rol)
        elif nombre and not fecha_ini and not fecha_fin and not id_votacion and not rol:
            censos = Censo.objects.filter(nombre=nombre)
        elif nombre and fecha_ini and not fecha_fin and not id_votacion and not rol:
            censos = Censo.objects.filter(nombre=nombre, fecha_ini=fecha_ini)
        elif nombre and fecha_ini and fecha_fin and not id_votacion and not rol:
            censos = Censo.objects.filter(nombre=nombre, fecha_ini=fecha_ini, fecha_fin=fecha_fin)
        elif nombre and fecha_ini and fecha_fin and id_votacion and not rol:
            censos = Censo.objects.filter(nombre=nombre, fecha_ini=fecha_ini, fecha_fin=fecha_fin,
                                          id_votacion=id_votacion)
        elif not nombre and fecha_ini and fecha_fin and id_votacion and rol:
            censos = Censo.objects.filter(fecha_ini=fecha_ini, fecha_fin=fecha_fin, id_votacion=id_votacion,
                                          rol=rol)
        elif not nombre and not fecha_ini and fecha_fin and id_votacion and rol:
            censos = Censo.objects.filter(fecha_fin=fecha_fin, id_votacion=id_votacion, rol=rol)
        elif not nombre and not fecha_ini and not fecha_fin and not id_votacion and rol:
            censos = Censo.objects.filter(rol=rol)
        elif nombre and not fecha_ini and not fecha_fin and not id_votacion and rol:
            censos = Censo.objects.filter(nombre=nombre, rol=rol)
        elif nombre and not fecha_ini and not fecha_fin and id_votacion and rol:
            censos = Censo.objects.filter(nombre=nombre, id_votacion=id_votacion, rol=rol)
        elif nombre and not fecha_ini and not fecha_fin and id_votacion and not rol:
            censos = Censo.objects.filter(nombre=nombre, id_votacion=id_votacion)
        elif nombre and id_votacion and rol and fecha_ini and not fecha_fin:
            censos = Censo.objects.filter(nombre=nombre, id_votacion=id_votacion, rol=rol,
                                          fecha_ini=fecha_ini)
        elif nombre and id_votacion and rol and rol and not fecha_ini and fecha_fin:
            censos = Censo.objects.filter(nombre=nombre, id_votacion=id_votacion, rol=rol,
                                          fecha_ini=fecha_ini)
        elif nombre and id_votacion and not rol and fecha_ini and not fecha_fin:
            censos = Censo.objects.filter(nombre=nombre, id_votacion=id_votacion, fecha_ini=fecha_ini)
        elif nombre and id_votacion and not rol and not fecha_ini and fecha_fin:
            censos = Censo.objects.filter(nombre=nombre, id_votacion=id_votacion, fecha_fin=fecha_fin)
        elif nombre and not id_votacion and rol and fecha_ini and fecha_fin:
            censos = Censo.objects.filter(nombre=nombre, rol=rol, fecha_fin=fecha_fin, fecha_ini=fecha_ini)
        elif nombre and not id_votacion and rol and fecha_ini and not fecha_fin:
            censos = Censo.objects.filter(nombre=nombre, rol=rol, fecha_ini=fecha_ini)
        elif nombre and not id_votacion and rol and not fecha_ini and fecha_fin:
            censos = Censo.objects.filter(nombre=nombre, rol=rol, fecha_fin=fecha_fin)
        elif nombre and not id_votacion and not rol and not fecha_ini and fecha_fin:
            censos = Censo.objects.filter(nombre=nombre, fecha_fin=fecha_fin)
        elif not nombre and id_votacion and rol and fecha_ini and not fecha_fin:
            censos = Censo.objects.filter(id_votacion=id_votacion, rol=rol, fecha_ini=fecha_ini)
        elif not nombre and id_votacion and rol and not fecha_ini and fecha_fin:
            censos = Censo.objects.filter(id_votacion=id_votacion, rol=rol, fecha_fin=fecha_fin)
        elif not nombre and id_votacion and rol and not fecha_ini and not fecha_fin:
            censos = Censo.objects.filter(id_votacion=id_votacion, rol=rol)
        elif not nombre and id_votacion and not rol and fecha_ini and fecha_fin:
            censos = Censo.objects.filter(id_votacion=id_votacion, fecha_ini=fecha_ini, fecha_fin=fecha_fin)
        elif not nombre and id_votacion and not rol and fecha_ini and not fecha_fin:
            censos = Censo.objects.filter(id_votacion=id_votacion, fecha_ini=fecha_ini)
        elif not nombre and id_votacion and not rol and not fecha_ini and fecha_fin:
            censos = Censo.objects.filter(id_votacion=id_votacion, fecha_fin=fecha_fin)
        elif not nombre and id_votacion and not rol and not fecha_ini and not fecha_fin:
            censos = Censo.objects.filter(id_votacion=id_votacion)
        elif not nombre and not id_votacion and rol and fecha_ini and fecha_fin:
            censos = Censo.objects.filter(rol=rol, fecha_ini=fecha_ini, fecha_fin=fecha_fin)
        elif not nombre and not id_votacion and rol and fecha_ini and not fecha_fin:
            censos = Censo.objects.filter(rol=rol, fecha_ini=fecha_ini)
        elif not nombre and not id_votacion and rol and not fecha_ini and fecha_fin:
            censos = Censo.objects.filter(rol=rol, fecha_fin=fecha_fin)
        elif not nombre and not id_votacion and not rol and fecha_ini and fecha_fin:
            censos = Censo.objects.filter(fecha_ini=fecha_ini, fecha_fin=fecha_fin)
        elif not nombre and not id_votacion and not rol and fecha_ini and not fecha_fin:
            censos = Censo.objects.filter(fecha_ini=fecha_ini)
        elif not nombre and not id_votacion and not rol and not fecha_ini and fecha_fin:

            censos = Censo.objects.filter(fecha_fin=fecha_fin)

    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    context = {'request': request}
    serializer = CensoSerializer(censos, context=context, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def can_vote(request):
    id_votacion = request.GET.get('id_votacion', '')
    username = request.GET.get('username', '')
    resultado = False

    # URL de autenticación aún sin especificar, cambiar para obtener la petición correcta
    url_autenticacion = 'http://autenticacion.nvotesus.es'
    # Obtenemos json de la petición de la api para ver el rol del usuario solicitado
    # r = requests.get('{0}/api/getRoleUser/{1}'.format(url_autenticacion, username))
    # json = r.json()
    # Transformamos el json a DICT para que así podamos acceder al dato que nos interesa, ROL
    # json_dict = json.loads(json)
    # A partir del rol, comprobamos que existe en nuestra base de datos un censo activo con ese rol y votación
    # rol = json_dict['
    rol = 'ASISTENTE'
    hoy = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resultado = Censo.objects.filter(rol=rol, fecha_ini__lte=hoy, fecha_fin__gte=hoy).exists()
    response_data = {'result': resultado}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@api_view(['GET'])
def create_censo(request):
    rol = request.GET.get('rol', '')
    id_votacion = request.GET.get('id_votacion', '')
    nombre = request.GET.get('nombre', '')
    fecha_ini = request.GET.get('fecha_ini', '')
    fecha_fin = request.GET.get('fecha_fin', '')

    if not nombre:
        nombre = 'Censo de ' + id_votacion + ' para el grupo ' + rol

    if not fecha_ini:
        fecha_ini = datetime.now()

    if not fecha_fin:
        fi = datetime.now()
        fa = datetime.timedelta(days=21)
        fecha_fin = fi + fa

    if rol and id_votacion:
        try:
            censo = Censo.objects.create(id_votacion=id_votacion, rol=rol, nombre=nombre, fecha_ini=fecha_ini,
                                         fecha_fin=fecha_fin)
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
    rol = request.GET.get('rol', Censo.objects.get(id=id).rol)
    idvotacion = request.GET.get('id_votacion', Censo.objects.get(id=id).id_votacion)
    fechaini = request.GET.get('fecha_ini', '')
    if not fechaini:
        fechaini = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fechafin = request.GET.get('fecha_fin', Censo.objects.get(id=id).fecha_fin)
    censo = None
    if id and Censo.objects.filter(id=id).exists():
        try:
            Censo.objects.filter(id=id).update(nombre=nombre, fecha_ini=fechaini, fecha_fin=fechafin, rol=rol,
                                               id_votacion=idvotacion)
            censo = Censo.objects.get(id=id)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
    context = {'request': request}
    serializer = CensoSerializer(censo, context=context)
    return Response(serializer.data)


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
