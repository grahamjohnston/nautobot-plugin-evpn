from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from nautobot.core.fields import AutoSlugField
from nautobot.core.models.generics import PrimaryModel


class EVPNService(PrimaryModel):
    name = models.CharField(max_length=25)
    slug = AutoSlugField(populate_from="name")
    vni = models.IntegerField(unique=True)
    description = models.CharField(max_length=200, blank=True)  # , default="")
    tenant = models.ForeignKey(
        to="tenancy.tenant", on_delete=models.RESTRICT, blank=True, null=True
    )

    class Meta:
        ordering = ["vni"]
        verbose_name = "EVPN Service"
        verbose_name_plural = "EVPN Services"

    def get_absolute_url(self):
        return reverse(
            "plugins:nautobot_plugin_evpn:evpn-service", kwargs={"pk": self.pk}
        )

    def __str__(self) -> str:
        return f"{self.name} with VNI {self.vni}"

    """
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        if not getattr(self, "name") or not getattr(self, "vni"):
            ValidationError("Must have a name and VNI value.")

        if not getattr(self, "description"):
            self.description = ""

        super().clean(*args, **kwargs)
"""
