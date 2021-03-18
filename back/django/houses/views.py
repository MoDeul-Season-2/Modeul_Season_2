from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HouseSerializer
from .models import House


class HouseView(APIView):

    def post(self, request):
        house_serializer = HouseSerializer(data=request.data)
        if house_serializer.is_valid():
            house_serializer.save()
            return Response(house_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(house_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        if kwargs.get('id') is None:
            house_queryset = House.objects.all()
            house_queryset_serializer = HouseSerializer(house_queryset, many=True)
            return Response(house_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('id')
            house_serializer = HouseSerializer(House.objects.get(id=id))
            return Response(house_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response('Invalid Request', status=status.HTTP_400_BAD_REQUEST)
        else:
            id = kwargs.get('id')
            house_object = House.objects.get(id=id)

            update_house_serializer = HouseSerializer(house_object, data=request.data)
            if update_house_serializer.is_valid():
                update_house_serializer.save()
                return Response(update_house_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response('Invalid Request', status=status.HTTP_400_BAD_REQUEST)
        else:
            id = kwargs.get('id')
            house_object = House.objects.get(id=id)
            house_object.delete()
            return Response("Deleted", status=status.HTTP_200_OK)
