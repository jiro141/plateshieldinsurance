from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TarjetaSeguroFloridaViewSet, CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'seguros', TarjetaSeguroFloridaViewSet, basename='seguros')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
