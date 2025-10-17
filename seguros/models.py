from django.db import models

class TarjetaSeguroFlorida(models.Model):
    nombre_asegurado = models.CharField(max_length=120, verbose_name="Nombre del Asegurado")
    direccion = models.CharField(max_length=200, verbose_name="Dirección del Asegurado")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    estado = models.CharField(max_length=10, verbose_name="Estado")
    codigo_postal = models.CharField(max_length=10, verbose_name="Código Postal", blank=True, null=True)
    telefono = models.CharField(max_length=20, verbose_name="Teléfono del Asegurado", blank=True, null=True)

    aseguradora = models.CharField(max_length=150, verbose_name="Aseguradora")
    numero_poliza = models.CharField(max_length=50, verbose_name="Número de Póliza")
    numero_vin = models.CharField(max_length=30, verbose_name="Número VIN del Vehículo")
    marca = models.CharField(max_length=50, verbose_name="Marca del Vehículo")
    modelo = models.CharField(max_length=100, verbose_name="Modelo del Vehículo")
    anio = models.PositiveIntegerField(verbose_name="Año del Vehículo")

    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio del Seguro")
    fecha_expiracion = models.DateField(verbose_name="Fecha de Expiración del Seguro")

    direccion_oficina = models.CharField(max_length=200, verbose_name="Dirección de la Oficina", blank=True, null=True)
    telefono_oficina = models.CharField(max_length=20, verbose_name="Teléfono de la Oficina", blank=True, null=True)

    advertencia_legal = models.TextField(verbose_name="Advertencia Legal", blank=True, null=True)

    # 🔹 Nuevos campos
    pago = models.BooleanField(default=False, verbose_name="Pago Realizado")  # True = pagado, False = pendiente
    link = models.URLField(max_length=500, blank=True, null=True, verbose_name="Enlace al Documento")

    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    class Meta:
        verbose_name = "Tarjeta de Seguro de Florida"
        verbose_name_plural = "Tarjetas de Seguro de Florida"
        db_table = "tarjeta_seguro_florida"
        ordering = ["-fecha_registro"]

    def __str__(self):
        return f"{self.nombre_asegurado} - {self.numero_poliza} ({self.marca} {self.modelo})"
