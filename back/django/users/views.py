from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User


class UserView(APIView):

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        if kwargs.get('id') is None:
            user_queryset = User.objects.all()
            user_queryset_serializer = UserSerializer(user_queryset, many=True)
            return Response(user_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('id')
            user_serializer = UserSerializer(User.objects.get(id=id))
            return Response(user_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response("invalid Request", status=status.HTTP_400_BAD_REQUEST)
        else:
            id = kwargs.get('id')
            user_object = User.objects.get(id=id)

            update_user_serializer = UserSerializer(user_object, data=request.data)
            if update_user_serializer.is_valid():
                update_user_serializer.save()
                return Response(update_user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid Request", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response('invalid Request', status=status.HTTP_400_BAD_REQUEST)
        else:
            id = kwargs.get('id')
            user_object = User.objects.get(id=id)
            user_object.delete()
            return Response("deleted", status=status.HTTP_200_OK)
