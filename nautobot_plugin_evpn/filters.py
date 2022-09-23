from nautobot.extras.filters import CreatedUpdatedFilterSet
from nautobot.utilities.filters import BaseFilterSet, SearchFilter

from nautobot_plugin_evpn.models import EVPNService


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
