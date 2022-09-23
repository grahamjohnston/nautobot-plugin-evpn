from nautobot.core.api import OrderedDefaultRouter

from nautobot_plugin_evpn.api.views import EVPNServiceViewSet

router = OrderedDefaultRouter()
router.register("evpn-service", EVPNServiceViewSet)

urlpatterns = router.urls
