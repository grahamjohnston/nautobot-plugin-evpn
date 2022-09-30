from nautobot.core.api import OrderedDefaultRouter

from nautobot_plugin_evpn.api.views import EVPNServiceViewSet, VNIViewSet

router = OrderedDefaultRouter()
router.register("evpnservice", EVPNServiceViewSet)
router.register("vni", VNIViewSet)

urlpatterns = router.urls
