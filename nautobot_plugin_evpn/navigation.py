from nautobot.core.apps import (
    NavMenuAddButton,
    NavMenuGroup,
    NavMenuItem,
    NavMenuImportButton,
    NavMenuTab,
)
from nautobot.extras.plugins import PluginMenuButton, PluginMenuItem
from nautobot.utilities.choices import ButtonColorChoices

menu_items = (
    NavMenuTab(
        name="EVPN",
        weight=150,
        groups=(
            NavMenuGroup(
                name="EVPN",
                weight=100,
                items=(
                    NavMenuItem(
                        link="plugins:nautobot_plugin_evpn:vni_list",
                        name="VNIs",
                        # permissions=["example_plugin.view_examplemodel"],
                        permissions=[],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_evpn:vni_add",
                                # permissions=[
                                #    "example_plugin.add_examplemodel",
                                # ],
                                permissions=[],
                            ),
                            # NavMenuImportButton(
                            #    link="plugins:example_plugin:examplemodel_import",
                            #    permissions=["example_plugin.add_examplemodel"],
                            # ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_plugin_evpn:evpn-layer2-vrf_list",
                        name="EVPN Layer 2 VRFs",
                        # permissions=["example_plugin.view_examplemodel"],
                        permissions=[],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_evpn:evpnlayer2vrf_add",
                                # permissions=[
                                #    "example_plugin.add_examplemodel",
                                # ],
                                permissions=[],
                            ),
                            # NavMenuImportButton(
                            #    link="plugins:example_plugin:examplemodel_import",
                            #    permissions=["example_plugin.add_examplemodel"],
                            # ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_plugin_evpn:evpnservice_list",
                        name="EVPN Services",
                        # permissions=["example_plugin.view_examplemodel"],
                        permissions=[],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_evpn:evpnservice_add",
                                # permissions=[
                                #    "example_plugin.add_examplemodel",
                                # ],
                                permissions=[],
                            ),
                            # NavMenuImportButton(
                            #    link="plugins:example_plugin:examplemodel_import",
                            #    permissions=["example_plugin.add_examplemodel"],
                            # ),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
