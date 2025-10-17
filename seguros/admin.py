from django.contrib import admin
from .models import TarjetaSeguroFlorida

@admin.register(TarjetaSeguroFlorida)
class TarjetaSeguroFloridaAdmin(admin.ModelAdmin):
    list_display = ("nombre_asegurado", "numero_poliza", "marca", "modelo", "fecha_inicio", "fecha_expiracion")
    search_fields = ("nombre_asegurado", "numero_poliza", "numero_vin")
    list_filter = ("aseguradora", "fecha_inicio", "fecha_expiracion")
