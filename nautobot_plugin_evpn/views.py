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


# VNI
class VNIListView(generic.ObjectListView):
    queryset = models.VNI.objects.all()
    filterset = filters.VNIFilterSet
    filterset_form = forms.VNIFilterForm
    table = tables.VNITable
    action_buttons = ("add",)


class VNIEditView(generic.ObjectEditView):
    queryset = models.VNI.objects.all()
    model_form = forms.VNIForm


class VNIBulkEditView(generic.BulkEditView):
    queryset = models.VNI.objects.all()
    filterset = filters.VNIFilterSet
    table = tables.VNITable
    form = forms.VNIBulkEditForm


class VNIBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VNI.objects.all()
    filterset = filters.VNIFilterSet
    table = tables.VNITable


class VNIDetailView(generic.ObjectView):
    queryset = models.VNI.objects.all()


class VNIDeleteView(generic.ObjectDeleteView):
    queryset = models.VNI.objects.all()


# EVPNLayer2
class EVPNLayer2VRFListView(generic.ObjectListView):
    queryset = models.EVPNLayer2VRF.objects.all()
    filterset = filters.EVPNLayer2VRFFilterSet
    filterset_form = forms.EVPNLayer2VRFFilterForm
    table = tables.EVPNLayer2VRFTable
    action_buttons = ("add",)


class EVPNLayer2VRFEditView(generic.ObjectEditView):
    queryset = models.EVPNLayer2VRF.objects.all()
    model_form = forms.EVPNLayer2VRFForm


class EVPNLayer2VRFBulkEditView(generic.BulkEditView):
    queryset = models.EVPNLayer2VRF.objects.all()
    filterset = filters.EVPNLayer2VRFFilterSet
    table = tables.EVPNLayer2VRFTable
    form = forms.EVPNLayer2VRFBulkEditForm


class EVPNLayer2VRFBulkDeleteView(generic.BulkDeleteView):
    queryset = models.EVPNLayer2VRF.objects.all()
    filterset = filters.EVPNLayer2VRFFilterSet
    table = tables.EVPNLayer2VRFTable


class EVPNLayer2VRFDetailView(generic.ObjectView):
    queryset = models.EVPNLayer2VRF.objects.all()


class EVPNLayer2VRFDeleteView(generic.ObjectDeleteView):
    queryset = models.EVPNLayer2VRF.objects.all()


# EVPNLayer3
class EVPNLayer3VRFListView(generic.ObjectListView):
    queryset = models.EVPNLayer3VRF.objects.all()
    filterset = filters.EVPNLayer3VRFFilterSet
    filterset_form = forms.EVPNLayer3VRFFilterForm
    table = tables.EVPNLayer3VRFTable
    action_buttons = ("add",)


class EVPNLayer3VRFEditView(generic.ObjectEditView):
    queryset = models.EVPNLayer3VRF.objects.all()
    model_form = forms.EVPNLayer3VRFForm


class EVPNLayer3VRFBulkEditView(generic.BulkEditView):
    queryset = models.EVPNLayer3VRF.objects.all()
    filterset = filters.EVPNLayer3VRFFilterSet
    table = tables.EVPNLayer3VRFTable
    form = forms.EVPNLayer3VRFBulkEditForm


class EVPNLayer3VRFBulkDeleteView(generic.BulkDeleteView):
    queryset = models.EVPNLayer3VRF.objects.all()
    filterset = filters.EVPNLayer3VRFFilterSet
    table = tables.EVPNLayer3VRFTable


class EVPNLayer3VRFDetailView(generic.ObjectView):
    queryset = models.EVPNLayer3VRF.objects.all()


class EVPNLayer3VRFDeleteView(generic.ObjectDeleteView):
    queryset = models.EVPNLayer3VRF.objects.all()


# EVPNAttachmentPoint
class EVPNAttachmentPointListView(generic.ObjectListView):
    queryset = models.EVPNAttachmentPoint.objects.all()
    filterset = filters.EVPNAttachmentPointFilterSet
    filterset_form = forms.EVPNAttachmentPointFilterForm
    table = tables.EVPNAttachmentPointTable
    action_buttons = ("add",)


class EVPNAttachmentPointEditView(generic.ObjectEditView):
    queryset = models.EVPNAttachmentPoint.objects.all()
    model_form = forms.EVPNAttachmentPointForm


class EVPNAttachmentPointBulkEditView(generic.BulkEditView):
    queryset = models.EVPNAttachmentPoint.objects.all()
    filterset = filters.EVPNAttachmentPointFilterSet
    table = tables.EVPNAttachmentPointTable
    form = forms.EVPNAttachmentPointBulkEditForm


class EVPNAttachmentPointBulkDeleteView(generic.BulkDeleteView):
    queryset = models.EVPNAttachmentPoint.objects.all()
    filterset = filters.EVPNAttachmentPointFilterSet
    table = tables.EVPNAttachmentPointTable


class EVPNAttachmentPointDetailView(generic.ObjectView):
    queryset = models.EVPNAttachmentPoint.objects.all()


class EVPNAttachmentPointDeleteView(generic.ObjectDeleteView):
    queryset = models.EVPNAttachmentPoint.objects.all()
