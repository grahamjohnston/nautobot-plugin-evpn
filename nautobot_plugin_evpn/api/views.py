from nautobot.core.api.views import ModelViewSet

from nautobot_plugin_evpn.api.serializers import EVPNServiceSerializer
from nautobot_plugin_evpn.models import EVPNService
from nautobot_plugin_evpn.filters import EVPNServiceFilterSet


class EVPNServiceViewSet(ModelViewSet):
    queryset = EVPNService.objects.all()
    serializer_class = EVPNServiceSerializer
    filterset_class = EVPNServiceFilterSet
