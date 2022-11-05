from tabnanny import verbose
import django_tables2 as tables
from nautobot.utilities.tables import BaseTable, ButtonsColumn, ToggleColumn

from nautobot_plugin_evpn.models import (
    EVPNService,
    EVPNLayer2VRF,
    VNI,
    EVPNLayer3VRF,
    EVPNAttachmentPoint,
    EVPNEthernetSegment,
    EVPNEthernetSegmentLAGInterface,
)


class EVPNServiceTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn()
    layer2_vrf = tables.LinkColumn(verbose_name="Layer 2 VRF")
    vni = tables.LinkColumn(verbose_name="VNI")
    layer3_vrf = tables.LinkColumn(verbose_name="Layer 3 VRF")
    tenant = tables.LinkColumn()
    actions = ButtonsColumn(EVPNService)  # , buttons=["edit", "delete"])

    class Meta(BaseTable.Meta):
        model = EVPNService
        fields = ["pk", "name", "layer2_vrf", "vni", "description", "layer3_vrf", "tenant"]


class EVPNLayer2VRFTable(BaseTable):
    pk = ToggleColumn()
    id = tables.LinkColumn(verbose_name="ID")
    vrf = tables.LinkColumn(verbose_name="VRF")
    type = tables.Column()
    encapsulation = tables.Column()
    description = tables.Column()
    actions = ButtonsColumn(EVPNLayer2VRF)  # , buttons=["edit", "delete"])

    class Meta(BaseTable.Meta):
        model = EVPNLayer2VRF
        fields = ["pk", "id", "vrf", "type", "encapsulation", "description"]


class EVPNLayer3VRFTable(BaseTable):
    pk = ToggleColumn()
    id = tables.LinkColumn(verbose_name="ID")
    vrf = tables.LinkColumn(verbose_name="VRF")
    type = tables.Column()
    encapsulation = tables.Column()
    vni = tables.LinkColumn(verbose_name="VNI")
    description = tables.Column()
    actions = ButtonsColumn(EVPNLayer3VRF)  # , buttons=["edit", "delete"])

    class Meta(BaseTable.Meta):
        model = EVPNLayer3VRF
        fields = ["pk", "id", "vrf", "type", "encapsulation", "vni", "description"]


class VNITable(BaseTable):
    pk = ToggleColumn()
    vni = tables.LinkColumn(verbose_name="VNI")
    description = tables.Column()
    evpnservice = tables.LinkColumn(accessor="evpnservice", verbose_name="EVPN Service")
    evpnlayer3vrf = tables.LinkColumn(accessor="evpnlayer3vrf", verbose_name="EVPN Layer 3 VRF")
    actions = ButtonsColumn(VNI)  # , buttons=["edit", "delete"])

    class Meta(BaseTable.Meta):
        model = VNI
        fields = ["pk", "vni", "description", "evpnservice"]


class EVPNAttachmentPointTable(BaseTable):
    pk = ToggleColumn()
    id = tables.LinkColumn(verbose_name="ID")
    evpn_service = tables.LinkColumn(verbose_name="EVPN Service")
    device = tables.LinkColumn(verbose_name="Device")
    interface = tables.LinkColumn(verbose_name="Interface")
    description = tables.Column()
    actions = ButtonsColumn(EVPNAttachmentPoint)  # , buttons=["edit", "delete"])

    class Meta(BaseTable.Meta):
        model = EVPNAttachmentPoint
        fields = ["pk", "id", "evpn_service", "device", "interface", "description"]


class EVPNEthernetSegmentTable(BaseTable):
    pk = ToggleColumn()
    esi = tables.LinkColumn(verbose_name="ESI")
    type = tables.Column()
    description = tables.Column()
    actions = ButtonsColumn(EVPNEthernetSegment)  # , buttons=["edit", "delete"])

    class Meta(BaseTable.Meta):
        model = EVPNEthernetSegment
        fields = ["pk", "esi", "type", "description"]


class EVPNEthernetSegmentLAGInterfaceTable(BaseTable):
    pk = ToggleColumn()
    id = tables.LinkColumn(verbose_name="ID")
    esi = tables.LinkColumn(verbose_name="ESI")
    device = tables.LinkColumn()
    interface = tables.LinkColumn()
    description = tables.Column()
    actions = ButtonsColumn(EVPNEthernetSegmentLAGInterface)  # , buttons=["edit", "delete"])

    class Meta(BaseTable.Meta):
        model = EVPNEthernetSegmentLAGInterface
        fields = ["pk", "id", "esi", "device", "interface", "description"]
