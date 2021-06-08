from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter
from .permissions import MyFirstPermission


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        permissions = []
        if self.action in ["list", "retrieve"]:
            permissions = [AllowAny]
        if self.action in ["create"]:
            permissions = [IsAuthenticated]
        if self.action in ["update", "partial_update", 'destroy']:
            permissions = [MyFirstPermission]

        return [p() for p in permissions]
