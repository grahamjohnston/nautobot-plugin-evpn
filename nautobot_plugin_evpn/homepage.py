from nautobot.core.apps import HomePageItem, HomePagePanel

from .models import EVPNService, VNI, EVPNLayer2VRF

layout = (
    HomePagePanel(
        name="EVPN",
        items=(
            HomePageItem(
                name="VNIs",
                model=VNI,
                weight=150,
                link="plugins:nautobot_plugin_evpn:vni_list",
                description="List VNIs",
                # permissions=["example_plugin.view_examplemodel"],
                permissions=[],
            ),
            HomePageItem(
                name="Layer 2 VRFs",
                model=EVPNLayer2VRF,
                weight=150,
                link="plugins:nautobot_plugin_evpn:evpn-layer2-vrf_list",
                description="List Layer 2 EVPN VRFs",
                # permissions=["example_plugin.view_examplemodel"],
                permissions=[],
            ),
            HomePageItem(
                name="EVPN Services",
                model=EVPNService,
                weight=150,
                link="plugins:nautobot_plugin_evpn:evpnservice_list",
                description="List EVPN Services.",
                # permissions=["example_plugin.view_examplemodel"],
                permissions=[],
            ),
        ),
    ),
)
