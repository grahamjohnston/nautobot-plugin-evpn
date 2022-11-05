from nautobot.extras.filters import CreatedUpdatedFilterSet
from nautobot.utilities.filters import BaseFilterSet, SearchFilter

from nautobot_plugin_evpn.models import (
    EVPNEthernetSegment,
    EVPNService,
    VNI,
    EVPNLayer2VRF,
    EVPNLayer3VRF,
    EVPNAttachmentPoint,
    EVPNEthernetSegmentLAGInterface,
)


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
        model = EVPNLayer2VRF
        fields = [
            "vrf",
            "description",
        ]


class EVPNLayer3VRFFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    q = SearchFilter(
        filter_predicates={
            "vrf": "icontains",
            "description": "icontains",
        },
    )

    class Meta:
        model = EVPNLayer3VRF
        fields = [
            "vrf",
            "description",
        ]


class EVPNAttachmentPointFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    q = SearchFilter(
        filter_predicates={
            "evpn_service": "icontains",
            "interface": "icontains",
            "description": "icontains",
        },
    )

    class Meta:
        model = EVPNAttachmentPoint
        fields = [
            "evpn_service",
            "interface",
            "description",
        ]


class EVPNEthernetSegmentFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    q = SearchFilter(
        filter_predicates={
            "esi": "icontains",
            "description": "icontains",
        },
    )

    class Meta:
        model = EVPNEthernetSegment
        fields = [
            "esi",
            "type",
            "description",
        ]


class EVPNEthernetSegmentLAGInterfaceFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    q = SearchFilter(
        filter_predicates={
            "esi": "icontains",
            "description": "icontains",
        },
    )

    class Meta:
        model = EVPNEthernetSegmentLAGInterface
        fields = [
            "esi",
            "device",
            "interface",
            "description",
        ]
