from nautobot.core.api.views import ModelViewSet

from nautobot_plugin_evpn.api.serializers import EVPNServiceSerializer, VNISerializer
from nautobot_plugin_evpn.models import EVPNService, VNI
from nautobot_plugin_evpn.filters import EVPNServiceFilterSet, VNIFilterSet


class EVPNServiceViewSet(ModelViewSet):
    queryset = EVPNService.objects.all()
    serializer_class = EVPNServiceSerializer
    filterset_class = EVPNServiceFilterSet


class VNIViewSet(ModelViewSet):
    queryset = VNI.objects.all()
    serializer_class = VNISerializer
    filterset_class = VNIFilterSet
