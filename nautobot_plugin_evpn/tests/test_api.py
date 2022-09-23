from unittest import skip
from nautobot.utilities.testing import APIViewTestCases


from nautobot_plugin_evpn.models import EVPNService


class EVPNServiceAPIViewTest(APIViewTestCases.APIViewTestCase):
    model = EVPNService
    create_data = [
        {"name": "Service4", "description": "EVPN Service Description 4", "vni": 10004},
        {"name": "Service5", "description": "EVPN Service Description 5", "vni": 10005},
    ]
    bulk_update_data = {"description": "test update description"}

    @classmethod
    def setUpTestData(cls) -> None:
        EVPNService.objects.create(name="Service7", description="woot", vni=10007)
        EVPNService.objects.create(name="Service8", description="woot", vni=10008)
        EVPNService.objects.create(name="Service9", description="woot", vni=10009)

    @skip("Not implemented")
    def test_list_objects_brief(self):
        pass
