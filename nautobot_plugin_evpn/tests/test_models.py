from django.test import TestCase
from django.db.utils import IntegrityError

from nautobot.tenancy.models import Tenant

from nautobot_plugin_evpn.models import EVPNService


class TestModels(TestCase):
    def setUp(self):
        self.tenant = Tenant.objects.create(name="Tenant 1", slug="tenant-1")

    def test_create_service(self):
        service: EVPNService = EVPNService.objects.create(name="Service 1", vni=10001)

        self.assertEqual(service.name, "Service 1")
        self.assertEqual(service.vni, 10001)

    def test_create_service_tenant(self):
        service: EVPNService = EVPNService.objects.create(
            name="Service 1", vni=10001, tenant=self.tenant
        )

        self.assertEqual(service.name, "Service 1")
        self.assertEqual(service.vni, 10001)
        self.assertEqual(service.tenant.id, self.tenant.id)

    def test_create_service_unique_vni(self):
        service1: EVPNService = EVPNService.objects.create(name="Service 1", vni=10001)

        try:
            service2: EVPNService = EVPNService.objects.create(
                name="Service 2", vni=10001
            )
        except IntegrityError:
            service2 = None

        if service2 is not None:
            self.assertTrue(False)
