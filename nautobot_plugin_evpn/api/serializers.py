from nautobot.core.api.serializers import ValidatedModelSerializer
from nautobot.tenancy.api.nested_serializers import NestedTenantSerializer
from rest_framework.serializers import CharField, IntegerField

from nautobot_plugin_evpn.models import EVPNService


class EVPNServiceSerializer(ValidatedModelSerializer):
    name = CharField()
    vni = IntegerField()
    description = CharField(required=False)
    tenant = NestedTenantSerializer(required=False)

    class Meta:
        model = EVPNService
        fields = "__all__"
