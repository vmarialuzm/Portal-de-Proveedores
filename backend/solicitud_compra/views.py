from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import DetalleSolicitudCompra
from .serializers import DetalleSolicitudCompraSerializer

class DetalleSolicitudCompraView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):

        if DetalleSolicitudCompra.objects.all().exists():
            solicitudes = DetalleSolicitudCompra.objects.all()
            serializer = DetalleSolicitudCompraSerializer(solicitudes, many=True)
            return Response({"ok": True, "data": serializer.data}, status=status.HTTP_200_OK)
        
        else:
            return Response({"error": "No purchase requests found"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        permission_classes = [AllowAny]
        serializer = DetalleSolicitudCompraSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True, "message": "TODO created"}, status=status.HTTP_201_CREATED)

        else:
            return Response({"ok": False, "message": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

