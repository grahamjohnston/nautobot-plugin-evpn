from nautobot.extras.filters import CreatedUpdatedFilterSet
from nautobot.utilities.filters import BaseFilterSet, SearchFilter

from nautobot_plugin_evpn.models import EVPNService, VNI


class VNIFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    q = SearchFilter(
        filter_predicates={
            "vni": "icontains",
            "description": "icontains",
        },
    )

    class Meta:
        model = VNI
        fields = [
            "vni",
            "description",
        ]


class EVPNServiceFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    q = SearchFilter(
        filter_predicates={
            "name": "icontains",
            "description": "icontains",
            "vni": "icontains",
        },
    )

    class Meta:
        model = EVPNService
        fields = [
            "name",
            "description",
            "vni",
            "tenant",
        ]


class EVPNLayer2VRFFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    q = SearchFilter(
        filter_predicates={
            "vrf": "icontains",
            "description": "icontains",
        },
    )

    class Meta:
        model = EVPNService
        fields = [
            "name",
            "description",
        ]
