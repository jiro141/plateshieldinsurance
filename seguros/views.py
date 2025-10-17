from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.db.models import Q
from .models import TarjetaSeguroFlorida
from .serializers import TarjetaSeguroFloridaSerializer


# 🔐 Token personalizado con info del usuario
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# 🧾 CRUD + búsqueda automática
class TarjetaSeguroFloridaViewSet(viewsets.ModelViewSet):
    queryset = TarjetaSeguroFlorida.objects.all()
    serializer_class = TarjetaSeguroFloridaSerializer
    permission_classes = [permissions.IsAuthenticated]

    # 🔒 Control de permisos por acción
    def get_permissions(self):
        """
        - 'buscar' es público (sin token)
        - Los demás requieren autenticación
        """
        if self.action == "buscar":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    # 🔎 Buscar por póliza, VIN o nombre
    @action(detail=False, methods=["get"], url_path="buscar")
    def buscar(self, request):
        query = request.query_params.get("q", "").strip()

        if not query:
            return Response(
                {"error": "Debe enviar un parámetro de búsqueda (?q=)"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        resultados = TarjetaSeguroFlorida.objects.filter(
            Q(nombre_asegurado__icontains=query)
            | Q(numero_poliza__icontains=query)
            | Q(numero_vin__icontains=query)
        )

        if not resultados.exists():
            return Response(
                {"mensaje": "No se encontraron resultados"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # ✅ Construimos la respuesta según pago
        data = []
        for seguro in resultados:
            item = {
                "nombre_asegurado": seguro.nombre_asegurado,
                "numero_poliza": seguro.numero_poliza,
                "numero_vin": seguro.numero_vin,
                "marca":seguro.marca,
                "modelo":seguro.modelo,
                "anio":seguro.anio
            }

            # Si el seguro está pagado y tiene link, lo incluimos
            if seguro.pago and seguro.link:
                item["link"] = seguro.link

            data.append(item)

        return Response(data, status=status.HTTP_200_OK)
