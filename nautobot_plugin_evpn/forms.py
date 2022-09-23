from django import forms
from nautobot.tenancy.models import Tenant
from nautobot.utilities.forms import (
    BootstrapMixin,
    DynamicModelChoiceField,
    BulkEditForm,
    SlugField,
)

from nautobot_plugin_evpn.models import EVPNService


class EVPNServiceForm(BootstrapMixin, forms.ModelForm):
    name = forms.CharField(label="Name")
    slug = SlugField()
    description = forms.CharField(required=False, label="Description")
    vni = forms.IntegerField(label="VNI")
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(), label="Tenant", required=False
    )

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
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(), label="Tenant", required=False
    )


class EVPNServiceBulkEditForm(BootstrapMixin, BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=EVPNService.objects.all(), widget=forms.MultipleHiddenInput
    )
    name = forms.CharField(required=False)
    # description = forms.CharField(required=False)
    # tenant = DynamicModelChoiceField(
    #    queryset=Tenant.objects.all(), label="Tenant", required=False
    # )

    class Meta:
        #    nullable_fields = ["tenant"]
        nullable_fields = []
