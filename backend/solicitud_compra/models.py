from django.db import models
from proveedores.models import Proveedores

class SolicitudCompra(models.Model):
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    producto = models.CharField(max_length=100)
    enlace_producto = models.URLField()
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.precio_total = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Solicitud de {self.producto} para {self.proveedor}"
