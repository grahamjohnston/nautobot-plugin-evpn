import django_tables2 as tables
from nautobot.utilities.tables import BaseTable, ButtonsColumn, ToggleColumn

from nautobot_plugin_evpn.models import EVPNService, EVPNLayer2VRF, VNI


class EVPNServiceTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn()
    tenant = tables.LinkColumn()
    actions = ButtonsColumn(EVPNService)  # , buttons=["edit", "delete"])

    class Meta(BaseTable.Meta):
        model = EVPNService
        fields = ["pk", "name", "description", "vni", "tenant"]


class EVPNLayer2VRFTable(BaseTable):
    pk = ToggleColumn()
    vrf = tables.LinkColumn(verbose_name="VRF")
    type = tables.Column()
    encapsulation = tables.Column()
    description = tables.Column()
    actions = ButtonsColumn(EVPNLayer2VRF)  # , buttons=["edit", "delete"])

    class Meta(BaseTable.Meta):
        model = EVPNLayer2VRF
        fields = ["pk", "vrf", "type", "encapsulation", "description"]


class VNITable(BaseTable):
    pk = ToggleColumn()
    vni = tables.LinkColumn(verbose_name="VNI")
    description = tables.Column()
    actions = ButtonsColumn(VNI)  # , buttons=["edit", "delete"])

    class Meta(BaseTable.Meta):
        model = VNI
        fields = ["pk", "vni", "description"]
