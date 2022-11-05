import re

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from nautobot.core.fields import AutoSlugField
from nautobot.core.models.generics import PrimaryModel
from nautobot.dcim.models.devices import Device, Interface


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
    evpn_service = models.ForeignKey(EVPNService, on_delete=models.RESTRICT)
    device = models.ForeignKey(Device, on_delete=models.RESTRICT)
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


class EVPNLayer3Interface(PrimaryModel):
    evpn_service = models.ForeignKey(EVPNService, on_delete=models.RESTRICT)
    device = models.ForeignKey(Device, on_delete=models.RESTRICT)
    interface = models.OneToOneField(Interface, on_delete=models.RESTRICT)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["evpn_service"]
        verbose_name = "EVPN Layer 3 Interface"
        verbose_name_plural = "EVPN Layer 3 Interfaces"

    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_evpn:evpnlayer3interface", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.pk}"


class EVPNEthernetSegment(PrimaryModel):
    ESI_TYPES = [
        (0, "Manual"),
        (1, "Auto from LACP"),
        (2, "Auto from STP"),
        (3, "MAC based"),
        (4, "Router ID based"),
        (5, "ASN Based"),
    ]

    type = models.IntegerField(choices=ESI_TYPES)
    esi = models.CharField(
        max_length=29, unique=True, null=True, blank=True, default=None, validators=[MinLengthValidator(29)]
    )
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["esi"]
        verbose_name = "EVPN Ethernet Segment Identifier"
        verbose_name_plural = "EVPN Segment Identifiers"

    def __str__(self) -> str:
        if self.esi and len(self.esi) > 0:
            return f"{self.esi}"
        else:
            return f"{self.ESI_TYPES[self.type][1]}"

    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_evpn:evpnethernetsegment", kwargs={"pk": self.pk})

    def clean(self):
        if self.esi:
            if not re.match("^[a-fA-F0-9]{2}(:[a-fA-F0-9]{2}){9}$", self.esi):
                raise ValidationError("ESI not a valid format, match be like 00:11:22:33:44:55:66:77:88:99.")

        if self.type == 0 and not re.match("^00:", self.esi):
            raise ValidationError("When ESI Type is Manual, ESI must start '00'.")

        if self.type == 1 and self.esi != None:
            raise ValidationError("When type is Auto from LACP, ESI must be left blank.")

        if self.type == 2 and self.esi != None:
            raise ValidationError("When type is Auto from STP, ESI must be left blank.")

        if self.type == 3 and self.esi != None and not re.match("^03:", self.esi):
            raise ValidationError(
                "When using a MAC based ESI type and manually specifying the value, it must start with '03'."
            )

        if self.type == 4 and self.esi != None and not re.match("^04:", self.esi):
            raise ValidationError(
                "When using a Router ID based ESI type and manually specifying the value, it must start with '04'."
            )

        if self.type == 5 and self.esi != None and not re.match("^05:", self.esi):
            raise ValidationError(
                "When using an ASN based ESI type and manually specifying the value, it must start with '05'."
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


# class EVPNVirtualAddresses(PrimaryModel):
#    EVPN_VIRTUAL_ADDRESS_TYPE = [("vga", "Virtual Gateway Address"), ("anycast", "Anycast Address")]
#    evpn_service = models.ForeignKey(EVPNService, on_delete=models.RESTRICT)
#    type = models.CharField(max_length=20, choices=EVPN_VIRTUAL_ADDRESS_TYPE)
#    ipv4_address=models.


class EVPNEthernetSegmentLAGInterface(PrimaryModel):
    esi = models.ForeignKey(EVPNEthernetSegment, on_delete=models.RESTRICT)
    device = models.ForeignKey(Device, on_delete=models.RESTRICT)
    interface = models.ForeignKey(Interface, on_delete=models.RESTRICT)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["esi"]
        verbose_name = "EVPN ESI-LAG"
        verbose_name_plural = "EVPN ESI-LAGs"

    def get_absolute_url(self):
        return reverse("plugins:nautobot_plugin_evpn:evpnethernetsegmentlaginterface", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.pk}"
