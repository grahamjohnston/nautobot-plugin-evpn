from nautobot.core.views import generic

from nautobot_plugin_evpn import models, forms, filters, tables


class EVPNServiceListView(generic.ObjectListView):
    queryset = models.EVPNService.objects.all()
    filterset = filters.EVPNServiceFilterSet
    filterset_form = forms.EVPNServiceFilterForm
    table = tables.EVPNServiceTable
    action_buttons = ("add",)


class EVPNServiceEditView(generic.ObjectEditView):
    queryset = models.EVPNService.objects.all()
    model_form = forms.EVPNServiceForm


class EVPNServiceBulkEditView(generic.BulkEditView):
    queryset = models.EVPNService.objects.all()
    filterset = filters.EVPNServiceFilterSet
    table = tables.EVPNServiceTable
    form = forms.EVPNServiceBulkEditForm


class EVPNServiceBulkDeleteView(generic.BulkDeleteView):
    queryset = models.EVPNService.objects.all()
    filterset = filters.EVPNServiceFilterSet
    table = tables.EVPNServiceTable


class EVPNServiceDetailView(generic.ObjectView):
    queryset = models.EVPNService.objects.all()


class EVPNServiceDeleteView(generic.ObjectDeleteView):
    queryset = models.EVPNService.objects.all()
