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


