from django.urls import path
from .views import DetalleSolicitudCompraView, SolicitudCompraView, DetalleSolicitudCompraIdView

urlpatterns = [
    path("", SolicitudCompraView.as_view(), name="solicitud"),
    path("detalle/", DetalleSolicitudCompraView.as_view(), name="detalle"),
    path("item_detalle/<id>/", DetalleSolicitudCompraIdView.as_view(), name="item-detalle")
]