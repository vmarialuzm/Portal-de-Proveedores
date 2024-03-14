from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import DetalleSolicitudCompra, SolicitudCompra
from .serializers import DetalleSolicitudCompraSerializer, SolicitudCompraSerializer

class SolicitudCompraView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        solicitudes = SolicitudCompra.objects.all()

        if solicitudes.exists():
            serializer = SolicitudCompraSerializer(solicitudes, many=True)
            return Response({"ok": True, "data": serializer.data}, status=status.HTTP_200_OK)
        
        else:
            return Response({"error": "No purchase requests found"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, format=None):
        serializer = SolicitudCompraSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True, "message": "Request created"}, status=status.HTTP_201_CREATED)

        else:
            return Response({"ok": False, "message": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


""" ********************************************************************************************************************** """


class DetalleSolicitudCompraView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        solicitud_id = request.query_params.get('solicitud_id')

        if solicitud_id is not None:
            detalles = DetalleSolicitudCompra.objects.filter(solicitud_compra_id=solicitud_id)
            serializer = DetalleSolicitudCompraSerializer(detalles, many=True)
            return Response({"ok": True, "data": serializer.data}, status=status.HTTP_200_OK)
        
        return Response({"error": "No detail purchase requests found"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, format=None):
        serializer = DetalleSolicitudCompraSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True, "message": "Detail Request Created"}, status=status.HTTP_201_CREATED)

        return Response({"ok": False, "message": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class DetalleSolicitudCompraIdView(APIView):
    def get(self, request, id, format=None):
        detalle = get_object_or_404(DetalleSolicitudCompra, pk=id)
        serializer = DetalleSolicitudCompraSerializer(detalle)
        return Response({"ok": True, "data": serializer.data}, status=status.HTTP_200_OK)
        
    def put(self, request, id, format=None):
        detalle = get_object_or_404(DetalleSolicitudCompra, pk=id)
        serializer = DetalleSolicitudCompraSerializer(detalle, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True, "message": "Detail Request Updated"}, status=status.HTTP_200_OK)
        
        return Response({"ok": False, "message": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, id, format=None):
        detalle = get_object_or_404(DetalleSolicitudCompra, pk=id)
        detalle.delete()
        return Response({"ok": True, "message": "Detail Request Delete"}, status=status.HTTP_200_OK)