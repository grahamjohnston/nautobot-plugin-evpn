import django_tables2 as tables
from nautobot.utilities.tables import BaseTable, ButtonsColumn, ToggleColumn

from nautobot_plugin_evpn.models import EVPNService


class EVPNServiceTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn()
    tenant = tables.LinkColumn()
    actions = ButtonsColumn(EVPNService)  # , buttons=["edit", "delete"])

    class Meta(BaseTable.Meta):
        model = EVPNService
        fields = ["pk", "name", "description", "vni", "tenant"]
