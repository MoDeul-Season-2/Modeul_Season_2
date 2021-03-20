from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ApplySerializer
from .models import Apply


class AppliesView(APIView):

    # POST /apply
    def post(self, request):
        if not request.apply.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = ApplySerializer(data=request.data)
            if serializer.is_valid():
                apply = serializer.save(apply=request.apply)
                apply_serializer = ApplySerializer(apply).data
                return Response(data=apply_serializer, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET /apply
    def get(self, request):
        apply = Apply.objects.all()
        serializer = ApplySerializer(apply, many=True).data
        return Response(serializer)


class ApplyView(APIView):

    def get_apply(self, pk):
        try:
            apply = Apply.objects.get(pk=pk)
            return apply
        except Apply.DoesNotExist:
            return None

    # GET /apply/{apply_id}
    def get(self, request, pk):
        apply = self.get_apply(pk)
        if apply is not None:
            serializer = ApplySerializer(apply).data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # PUT /apply/{apply_id}
    def put(self, request, pk):
        apply = self.get_apply(pk)
        if apply is not None:
            if apply.host != request.user or apply.guest != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = ApplySerializer(apply, data=request.data, partial=True)
            if serializer.is_valid():
                apply = serializer.save()
                return Response(ApplySerializer(apply).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # DELETE /apply/{apply_id}
    def delete(self, request, pk):
        apply = self.get_apply(pk)
        if apply is not None:
            if apply.host != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            apply.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)