from enum import unique
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from nautobot.core.fields import AutoSlugField
from nautobot.core.models.generics import PrimaryModel
from nautobot.dcim.models.devices import Interface


class VNI(PrimaryModel):
    vni = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(16777216)], unique=True)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["vni"]
        verbose_name = "VXLAN VNI"
        verbose_name_plural = "VXLAN VNIs"

    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_evpn:vni", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.vni}"


class EVPNLayer2VRF(PrimaryModel):
    EVPN_VRF_TYPES = [("vlan_aware", "VLAN Aware Bundle")]
    EVPN_ENCAPSULATION = [("vxlan", "VXLAN")]

    vrf = models.OneToOneField("ipam.vrf", on_delete=models.RESTRICT)
    type = models.CharField(max_length=20, choices=EVPN_VRF_TYPES)
    encapsulation = models.CharField(max_length=20, choices=EVPN_ENCAPSULATION)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["vrf"]
        verbose_name = "EVPN Layer 2 VRF"
        verbose_name_plural = "EVPN Layer 2 VRFs"

    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_evpn:evpnlayer2vrf", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.vrf}"


class EVPNLayer3VRF(PrimaryModel):
    EVPN_VRF_TYPES = [("evpn_l3", "EVPN L3VPN")]
    EVPN_ENCAPSULATION = [("vxlan", "VXLAN")]

    type = models.CharField(max_length=20, choices=EVPN_VRF_TYPES)
    encapsulation = models.CharField(max_length=20, choices=EVPN_ENCAPSULATION)
    vrf = models.OneToOneField("ipam.vrf", on_delete=models.RESTRICT)
    vni = models.OneToOneField(VNI, on_delete=models.RESTRICT)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["vrf"]
        verbose_name = "EVPN Layer 3 VRF"
        verbose_name_plural = "EVPN Layer 3 VRFs"

    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_evpn:evpnlayer3vrf", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.vrf}"


class EVPNService(PrimaryModel):
    name = models.CharField(max_length=25)
    slug = AutoSlugField(populate_from="name")
    layer2_vrf = models.ForeignKey(EVPNLayer2VRF, on_delete=models.RESTRICT)
    vni = models.OneToOneField(VNI, on_delete=models.RESTRICT)
    layer3_vrf = models.ForeignKey(EVPNLayer3VRF, on_delete=models.RESTRICT, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True)
    tenant = models.ForeignKey(to="tenancy.tenant", on_delete=models.RESTRICT, blank=True, null=True)

    class Meta:
        ordering = ["vni"]
        verbose_name = "EVPN Service"
        verbose_name_plural = "EVPN Services"

    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_evpn:evpnservice", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.name}"


class EVPNAttachmentPoint(PrimaryModel):
    evpn_service = models.OneToOneField(EVPNService, on_delete=models.RESTRICT)
    interface = models.OneToOneField(Interface, on_delete=models.RESTRICT)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["evpn_service"]
        verbose_name = "EVPN Attachment Point"
        verbose_name_plural = "EVPN Attachment Points"

    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_evpn:evpnattachmentpoint", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.pk}"
