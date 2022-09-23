# Uncomment the following to enable data manipulation within the admin portal
"""
from django.contrib import admin

from nautobot.core.admin import admin_site

from .models import EVPNService


@admin.register(EVPNService, site=admin_site)
class EVPNServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "vni", "tenant")
"""
