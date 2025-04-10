from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class AbstractViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=['GET', 'POST'])
    def activos(self, request):
        activos = self.queryset.filter(activo=True)
        serializer = self.get_serializer(activos, many=True)
        return Response(serializer.data)


class AbstractAPIView(APIView):
    permission_classes = (IsAuthenticated,)
