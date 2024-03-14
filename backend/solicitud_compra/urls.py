from django.urls import path
from .views import DetalleSolicitudCompraView

urlpatterns = [
    path("", DetalleSolicitudCompraView.as_view(), name="solicitud"),
    
]