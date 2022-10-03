from nautobot.core.apps import HomePageItem, HomePagePanel

from .models import EVPNAttachmentPoint, EVPNService, VNI, EVPNLayer2VRF, EVPNLayer3VRF

layout = (
    HomePagePanel(
        name="EVPN",
        items=(
            HomePageItem(
                name="VNIs",
                model=VNI,
                weight=150,
                link="plugins:nautobot_plugin_evpn:vni_list",
                description="VXLAN Virtual Network Identifiers",
                # permissions=["example_plugin.view_examplemodel"],
                permissions=[],
            ),
            HomePageItem(
                name="Layer 2 VRFs",
                model=EVPNLayer2VRF,
                weight=150,
                link="plugins:nautobot_plugin_evpn:evpnlayer2vrf_list",
                description="EVPN Layer 2 VRFs",
                # permissions=["example_plugin.view_examplemodel"],
                permissions=[],
            ),
            HomePageItem(
                name="Layer 3 VRFs",
                model=EVPNLayer3VRF,
                weight=150,
                link="plugins:nautobot_plugin_evpn:evpnlayer3vrf_list",
                description="EVPN Layer 3 VRFs",
                # permissions=["example_plugin.view_examplemodel"],
                permissions=[],
            ),
            HomePageItem(
                name="EVPN Services",
                model=EVPNService,
                weight=150,
                link="plugins:nautobot_plugin_evpn:evpnservice_list",
                description="EVPN Services Instances",
                # permissions=["example_plugin.view_examplemodel"],
                permissions=[],
            ),
            HomePageItem(
                name="EVPN Service Attachment Points",
                model=EVPNAttachmentPoint,
                weight=150,
                link="plugins:nautobot_plugin_evpn:evpnattachmentpoint_list",
                description="EVPN Service Attachment Points",
                # permissions=["example_plugin.view_examplemodel"],
                permissions=[],
            ),
        ),
    ),
)
