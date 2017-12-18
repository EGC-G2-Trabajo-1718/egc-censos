from .models import Censo
from .serializers import CensoSerializer
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


def delete_censo(request):
    @api_view(['delete'])
    def delete_censo(request):
        idRespuesta = request.GET.get('id', '')

        if Censo.objects.filter(id=idRespuesta).exists():
            Censo.objetcts.filter(id=idRespuesta).delete()
            deleted = ExitSerializer.serializer_field_mapping("True", "El censo ha sido eliminado")
            return HttpResponse(content=deleted, mimetype='application/json')

        else:
            notDeleted = ExitSerializer.serializer_field_mapping("False", "El censo no se ha podido eliminar")
            return HttpResponse(content=notDeleted, mimetype='application/json')

