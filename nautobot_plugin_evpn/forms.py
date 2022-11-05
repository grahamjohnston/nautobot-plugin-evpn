from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from nautobot.ipam.models import VRF
from nautobot.tenancy.models import Tenant
from nautobot.dcim.models import Device
from nautobot.dcim.models.devices import Interface
from nautobot.utilities.forms import (
    BootstrapMixin,
    DynamicModelChoiceField,
    BulkEditForm,
    SlugField,
)
from nautobot.extras.forms import RelationshipModelFormMixin

from nautobot_plugin_evpn.models import (
    EVPNService,
    VNI,
    EVPNLayer2VRF,
    EVPNLayer3VRF,
    EVPNAttachmentPoint,
    EVPNEthernetSegment,
    EVPNEthernetSegmentLAGInterface,
)

# VNI
class VNIForm(BootstrapMixin, forms.ModelForm):
    vni = forms.IntegerField(label="VNI", validators=[MinValueValidator(1), MaxValueValidator(16777216)])
    description = forms.CharField(required=False, label="Description")

    class Meta:
        model = VNI
        fields = ["vni", "description"]


class VNIFilterForm(BootstrapMixin, forms.Form):
    model = VNI
    q = forms.CharField(required=False, label="Search")
    vni = forms.IntegerField(
        label="VNI", validators=[MinValueValidator(1), MaxValueValidator(16777216)], required=False
    )
    description = forms.CharField(label="Description", required=False)


class VNIBulkEditForm(BootstrapMixin, BulkEditForm):
    pk = forms.ModelMultipleChoiceField(queryset=VNI.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        nullable_fields = ["description"]


class EVPNLayer2VRFForm(BootstrapMixin, forms.ModelForm):
    vrf = DynamicModelChoiceField(queryset=VRF.objects.all(), label="VRF", required=False)
    type = forms.ChoiceField(choices=EVPNLayer2VRF.EVPN_VRF_TYPES, label="Type")
    encapsulation = forms.ChoiceField(choices=EVPNLayer2VRF.EVPN_ENCAPSULATION, label="Encapsulation")
    description = forms.CharField(max_length=200, required=False)

    class Meta:
        model = EVPNLayer2VRF
        fields = ["vrf", "type", "encapsulation", "description"]


class EVPNLayer2VRFFilterForm(BootstrapMixin, forms.Form):
    model = EVPNLayer2VRF
    q = forms.CharField(required=False, label="Search")
    # vni = forms.IntegerField(
    #    label="EVPN Layer2 VRF", validators=[MinValueValidator(1), MaxValueValidator(16777216)], required=False
    # )
    description = forms.CharField(label="Description", required=False)


class EVPNLayer2VRFBulkEditForm(BootstrapMixin, BulkEditForm):
    pk = forms.ModelMultipleChoiceField(queryset=EVPNLayer2VRF.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        nullable_fields = ["description"]


class EVPNLayer3VRFForm(BootstrapMixin, forms.ModelForm):
    vrf = DynamicModelChoiceField(queryset=VRF.objects.all(), label="VRF", required=False)
    type = forms.ChoiceField(choices=EVPNLayer3VRF.EVPN_VRF_TYPES, label="Type")
    encapsulation = forms.ChoiceField(choices=EVPNLayer3VRF.EVPN_ENCAPSULATION, label="Encapsulation")
    vni = DynamicModelChoiceField(queryset=VNI.objects.all(), label="VNI", required=False)
    description = forms.CharField(max_length=200, required=False)

    class Meta:
        model = EVPNLayer3VRF
        fields = ["vrf", "type", "encapsulation", "vni", "description"]


class EVPNLayer3VRFFilterForm(BootstrapMixin, forms.Form):
    model = EVPNLayer3VRF
    q = forms.CharField(required=False, label="Search")
    # vni = forms.IntegerField(
    #    label="EVPN Layer2 VRF", validators=[MinValueValidator(1), MaxValueValidator(16777216)], required=False
    # )
    description = forms.CharField(label="Description", required=False)


class EVPNLayer3VRFBulkEditForm(BootstrapMixin, BulkEditForm):
    pk = forms.ModelMultipleChoiceField(queryset=EVPNLayer3VRF.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        nullable_fields = ["description"]


class EVPNServiceForm(BootstrapMixin, forms.ModelForm):
    name = forms.CharField(label="Name")
    slug = SlugField()
    # layer2_vrf = DynamicModelChoiceField(queryset=EVPNLayer2VRF.objects.all(), label="EVPN Layer 2 VRF")
    vni = DynamicModelChoiceField(queryset=VNI.objects.all(), label="VNI")
    # layer3_vrf = DynamicModelChoiceField(queryset=EVPNLayer3VRF.objects.all(), label="EVPN Layer 3 VRF")
    description = forms.CharField(required=False, label="Description")
    tenant = DynamicModelChoiceField(queryset=Tenant.objects.all(), label="Tenant", required=False)

    class Meta:
        model = EVPNService
        fields = ["name", "slug", "description", "vni", "tenant"]

    """
    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance")
        initial = kwargs.get("initial", {}).copy()

        if instance.name != "":
            initial["name"] = instance.name

        if instance.description != "":
            initial["description"] = instance.description

        if instance.vni != "":
            initial["vni"] = instance.vni

        # if instance.tenant != "":
        #    initial["tenant"] = instance.tenant

        kwargs["initial"] = initial

        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()

        self.instance.name = self.cleaned_data.get("name")
        self.instance.description = self.cleaned_data.get("description")
        self.instance.vni = self.cleaned_data.get("vni")
"""


class EVPNServiceFilterForm(BootstrapMixin, forms.Form):
    model = EVPNService
    q = forms.CharField(required=False, label="Search")
    name = forms.CharField(label="Name", required=False)
    # description = forms.CharField(label="Description", required=False)
    vni = forms.IntegerField(label="VNI", required=False)
    tenant = DynamicModelChoiceField(queryset=Tenant.objects.all(), label="Tenant", required=False)


class EVPNServiceBulkEditForm(BootstrapMixin, BulkEditForm):
    pk = forms.ModelMultipleChoiceField(queryset=EVPNService.objects.all(), widget=forms.MultipleHiddenInput)
    name = forms.CharField(required=False)
    # description = forms.CharField(required=False)
    # tenant = DynamicModelChoiceField(
    #    queryset=Tenant.objects.all(), label="Tenant", required=False
    # )

    class Meta:
        #    nullable_fields = ["tenant"]
        nullable_fields = []


class EVPNAttachmentPointForm(
    BootstrapMixin,
    RelationshipModelFormMixin,
    # forms.ModelForm,
):
    evpn_service = DynamicModelChoiceField(queryset=EVPNService.objects.all(), label="EVPN Service")
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        label="Device",
        initial_params={"interfaces": "$interface"},
    )
    interface = DynamicModelChoiceField(
        queryset=Interface.objects.all(),
        label="Interface",
        query_params={"device_id": "$device"},
    )
    description = forms.CharField(max_length=200, required=False)

    class Meta:
        model = EVPNAttachmentPoint
        fields = ["evpn_service", "device", "interface", "description"]


class EVPNAttachmentPointFilterForm(BootstrapMixin, forms.Form):
    model = EVPNAttachmentPoint
    q = forms.CharField(required=False, label="Search")
    # vni = forms.IntegerField(
    #    label="EVPN Layer2 VRF", validators=[MinValueValidator(1), MaxValueValidator(16777216)], required=False
    # )
    description = forms.CharField(label="Description", required=False)


class EVPNAttachmentPointBulkEditForm(BootstrapMixin, BulkEditForm):
    pk = forms.ModelMultipleChoiceField(queryset=EVPNAttachmentPoint.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        nullable_fields = ["description"]


# EVPN Ethernet Segment
class EVPNEthernetSegmentForm(
    BootstrapMixin,
    forms.ModelForm,
):
    type = forms.ChoiceField(choices=EVPNEthernetSegment.ESI_TYPES, label="Type")
    esi = forms.CharField(min_length=29, max_length=29, label="ESI", required=False, empty_value=None)
    description = forms.CharField(max_length=200, required=False)

    class Meta:
        model = EVPNEthernetSegment
        fields = ["type", "esi", "description"]


class EVPNEthernetSegmentFilterForm(BootstrapMixin, forms.Form):
    model = EVPNEthernetSegment
    q = forms.CharField(required=False, label="Search")
    esi = forms.CharField(label="ESI", required=False)
    description = forms.CharField(label="Description", required=False)


class EVPNEthernetSegmentBulkEditForm(BootstrapMixin, BulkEditForm):
    pk = forms.ModelMultipleChoiceField(queryset=EVPNEthernetSegment.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        nullable_fields = ["description"]


# EVPN Ethernet Segment LAG Interface


class EVPNEthernetSegmentLAGInterfaceForm(
    BootstrapMixin,
    RelationshipModelFormMixin,
):

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        label="Device",
        initial_params={"interfaces": "$interface"},
    )
    interface = DynamicModelChoiceField(
        queryset=Interface.objects.all(),
        label="Interface",
        query_params={"device_id": "$device"},
    )

    description = forms.CharField(max_length=200, required=False)

    class Meta:
        model = EVPNEthernetSegmentLAGInterface
        fields = ["esi", "device", "interface", "description"]


class EVPNEthernetSegmentLAGInterfaceFilterForm(BootstrapMixin, forms.Form):
    model = EVPNEthernetSegmentLAGInterface
    q = forms.CharField(required=False, label="Search")
    esi = forms.CharField(label="ESI", required=False)
    description = forms.CharField(label="Description", required=False)


class EVPNEthernetSegmentLAGInterfaceBulkEditForm(BootstrapMixin, BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=EVPNEthernetSegmentLAGInterface.objects.all(), widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(required=False)

    class Meta:
        nullable_fields = ["description"]
