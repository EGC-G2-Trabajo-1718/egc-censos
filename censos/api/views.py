from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_censo(request):
    pk = request.GET.get('id', '')
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    context = {'request': request}
    serializer = UserSerializer(user, context=context)
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
    return None

