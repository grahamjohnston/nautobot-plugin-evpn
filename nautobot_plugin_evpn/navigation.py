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
                        link="plugins:nautobot_plugin_evpn:evpnethernetsegment_list",
                        name="ESIs",
                        # permissions=["example_plugin.view_examplemodel"],
                        permissions=[],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_evpn:evpnethernetsegment_add",
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
                        link="plugins:nautobot_plugin_evpn:evpnlayer2vrf_list",
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
                        link="plugins:nautobot_plugin_evpn:evpnlayer3vrf_list",
                        name="EVPN Layer 3 VRFs",
                        # permissions=["example_plugin.view_examplemodel"],
                        permissions=[],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_evpn:evpnlayer3vrf_add",
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
                    NavMenuItem(
                        link="plugins:nautobot_plugin_evpn:evpnattachmentpoint_list",
                        name="EVPN Attachment Points",
                        # permissions=["example_plugin.view_examplemodel"],
                        permissions=[],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_evpn:evpnattachmentpoint_add",
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
                        link="plugins:nautobot_plugin_evpn:evpnethernetsegmentlaginterface_list",
                        name="EVPN ESI-LAG Interfaces",
                        # permissions=["example_plugin.view_examplemodel"],
                        permissions=[],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_evpn:evpnethernetsegmentlaginterface_add",
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
