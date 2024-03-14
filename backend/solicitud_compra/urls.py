from django.urls import path
from .views import DetalleSolicitudCompraView, SolicitudCompraView

urlpatterns = [
    path("", SolicitudCompraView.as_view(), name="solicitud"),
    path("detalle/", DetalleSolicitudCompraView.as_view(), name="detalle_solicitud"),
    
]