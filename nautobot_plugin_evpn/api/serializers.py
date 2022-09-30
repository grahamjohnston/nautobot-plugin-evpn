from nautobot.core.api.serializers import ValidatedModelSerializer
from nautobot.tenancy.api.nested_serializers import NestedTenantSerializer
from rest_framework.serializers import CharField, IntegerField

from nautobot_plugin_evpn.models import EVPNService, VNI


class EVPNServiceSerializer(ValidatedModelSerializer):
    name = CharField()
    slug = CharField()
    layer2_vrf = CharField()
    vni = CharField()
    layer3_vrf = CharField()
    description = CharField(required=False)
    tenant = NestedTenantSerializer(required=False)

    class Meta:
        model = EVPNService
        fields = "__all__"


class VNISerializer(ValidatedModelSerializer):
    vni = IntegerField()
    description = CharField(required=False)

    class Meta:
        model = VNI
        fields = "__all__"
