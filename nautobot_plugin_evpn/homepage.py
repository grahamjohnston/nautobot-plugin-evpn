from nautobot.core.apps import HomePageItem, HomePagePanel

from .models import EVPNService

layout = (
    HomePagePanel(
        name="EVPN",
        items=(
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
