from nautobot.extras.plugins import PluginConfig

__version__ = "0.1.0"


class EvpnPlugin(PluginConfig):
    name = "nautobot_plugin_evpn"
    verbose_name = "Nautobot plugin to model EVPN services"
    author = "grahamjohnston"
    description = "Plugin developed around EVPN-VXLAN using VLAN aware bundles"
    base_url = "evpn"
    required_settings = []
    default_settings = {}
    min_version = "1.4.2"
    max_version = "1.9999"
    caching_config = {}


config = EvpnPlugin
