from django.urls import path
from nautobot.extras.views import ObjectChangeLogView, ObjectNotesView
from nautobot_plugin_evpn import models, views

app_name = "evpn"

urlpatterns = [
    # EVPNService
    path("evpnservice/", views.EVPNServiceListView.as_view(), name="evpnservice_list"),
    path(
        "evpnservice/add/",
        views.EVPNServiceEditView.as_view(),
        name="evpnservice_add",
    ),
    path(
        "evpnservice/edit/",
        views.EVPNServiceBulkEditView.as_view(),
        name="evpnservice_bulk_edit",
    ),
    path(
        "evpnservice/delete/",
        views.EVPNServiceBulkDeleteView.as_view(),
        name="evpnservice_bulk_delete",
    ),
    path(
        "evpnservice/<uuid:pk>/",
        views.EVPNServiceDetailView.as_view(),
        name="evpnservice",
    ),
    path(
        "evpnservice/<uuid:pk>/edit/",
        views.EVPNServiceEditView.as_view(),
        name="evpnservice_edit",
    ),
    path(
        "evpnservice/<uuid:pk>/delete/",
        views.EVPNServiceDeleteView.as_view(),
        name="evpnservice_delete",
    ),
    path(
        "evpnservice/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="evpnservice_changelog",
        kwargs={"model": models.EVPNService},
    ),
    path(
        "evpnservice/<uuid:pk>/notes/",
        ObjectNotesView.as_view(),
        name="evpnservice_notes",
        kwargs={"model": models.EVPNService},
    ),
    # VNI
    path("vni/", views.VNIListView.as_view(), name="vni_list"),
    path(
        "vni/add/",
        views.VNIEditView.as_view(),
        name="vni_add",
    ),
    path(
        "vni/edit/",
        views.VNIBulkEditView.as_view(),
        name="vni_bulk_edit",
    ),
    path(
        "vni/delete/",
        views.VNIBulkDeleteView.as_view(),
        name="vni_bulk_delete",
    ),
    path(
        "vni/<uuid:pk>/",
        views.VNIDetailView.as_view(),
        name="vni",
    ),
    path(
        "vni/<uuid:pk>/edit/",
        views.VNIEditView.as_view(),
        name="vni_edit",
    ),
    path(
        "vni/<uuid:pk>/delete/",
        views.VNIDeleteView.as_view(),
        name="vni_delete",
    ),
    path(
        "vni/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="vni_changelog",
        kwargs={"model": models.VNI},
    ),
    path(
        "vni/<uuid:pk>/notes/",
        ObjectNotesView.as_view(),
        name="vni_notes",
        kwargs={"model": models.VNI},
    ),
    # EVPNLayer2VRF
    path("evpnlayer2vrf/", views.EVPNLayer2VRFListView.as_view(), name="evpnlayer2vrf_list"),
    path(
        "evpnlayer2vrf/add/",
        views.EVPNLayer2VRFEditView.as_view(),
        name="evpnlayer2vrf_add",
    ),
    path(
        "evpnlayer2vrf/edit/",
        views.EVPNLayer2VRFBulkEditView.as_view(),
        name="evpnlayer2vrf_bulk_edit",
    ),
    path(
        "evpnlayer2vrf/delete/",
        views.EVPNLayer2VRFBulkDeleteView.as_view(),
        name="evpnlayer2vrf_bulk_delete",
    ),
    path(
        "evpnlayer2vrf/<uuid:pk>/",
        views.EVPNLayer2VRFDetailView.as_view(),
        name="evpnlayer2vrf",
    ),
    path(
        "evpnlayer2vrf/<uuid:pk>/edit/",
        views.EVPNLayer2VRFEditView.as_view(),
        name="evpnlayer2vrf_edit",
    ),
    path(
        "evpnlayer2vrf/<uuid:pk>/delete/",
        views.EVPNLayer2VRFDeleteView.as_view(),
        name="evpnlayer2vrf_delete",
    ),
    path(
        "evpnlayer2vrf/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="evpnlayer2vrf_changelog",
        kwargs={"model": models.EVPNLayer2VRF},
    ),
    path(
        "evpnlayer2vrf/<uuid:pk>/notes/",
        ObjectNotesView.as_view(),
        name="evpnlayer2vrf_notes",
        kwargs={"model": models.EVPNLayer2VRF},
    ),
    # EVPNLayer3VRF
    path("evpnlayer3vrf/", views.EVPNLayer3VRFListView.as_view(), name="evpnlayer3vrf_list"),
    path(
        "evpnlayer3vrf/add/",
        views.EVPNLayer3VRFEditView.as_view(),
        name="evpnlayer3vrf_add",
    ),
    path(
        "evpnlayer3vrf/edit/",
        views.EVPNLayer3VRFBulkEditView.as_view(),
        name="evpnlayer3vrf_bulk_edit",
    ),
    path(
        "evpnlayer3vrf/delete/",
        views.EVPNLayer3VRFBulkDeleteView.as_view(),
        name="evpnlayer3vrf_bulk_delete",
    ),
    path(
        "evpnlayer3vrf/<uuid:pk>/",
        views.EVPNLayer3VRFDetailView.as_view(),
        name="evpnlayer3vrf",
    ),
    path(
        "evpnlayer3vrf/<uuid:pk>/edit/",
        views.EVPNLayer3VRFEditView.as_view(),
        name="evpnlayer3vrf_edit",
    ),
    path(
        "evpnlayer3vrf/<uuid:pk>/delete/",
        views.EVPNLayer3VRFDeleteView.as_view(),
        name="evpnlayer3vrf_delete",
    ),
    path(
        "evpnlayer3vrf/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="evpnlayer3vrf_changelog",
        kwargs={"model": models.EVPNLayer3VRF},
    ),
    path(
        "evpnlayer3vrf/<uuid:pk>/notes/",
        ObjectNotesView.as_view(),
        name="evpnlayer3vrf_notes",
        kwargs={"model": models.EVPNLayer3VRF},
    ),
    # EVPNAttachmentPoint
    path("evpnattachmentpoint/", views.EVPNAttachmentPointListView.as_view(), name="evpnattachmentpoint_list"),
    path(
        "evpnattachmentpoint/add/",
        views.EVPNAttachmentPointEditView.as_view(),
        name="evpnattachmentpoint_add",
    ),
    path(
        "evpnattachmentpoint/edit/",
        views.EVPNAttachmentPointBulkEditView.as_view(),
        name="evpnattachmentpoint_bulk_edit",
    ),
    path(
        "evpnattachmentpoint/delete/",
        views.EVPNAttachmentPointBulkDeleteView.as_view(),
        name="evpnattachmentpoint_bulk_delete",
    ),
    path(
        "evpnattachmentpoint/<uuid:pk>/",
        views.EVPNAttachmentPointDetailView.as_view(),
        name="evpnattachmentpoint",
    ),
    path(
        "evpnattachmentpoint/<uuid:pk>/edit/",
        views.EVPNAttachmentPointEditView.as_view(),
        name="evpnattachmentpoint_edit",
    ),
    path(
        "evpnattachmentpoint/<uuid:pk>/delete/",
        views.EVPNAttachmentPointDeleteView.as_view(),
        name="evpnattachmentpoint_delete",
    ),
    path(
        "evpnattachmentpoint/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="evpnattachmentpoint_changelog",
        kwargs={"model": models.EVPNAttachmentPoint},
    ),
    path(
        "evpnattachmentpoint/<uuid:pk>/notes/",
        ObjectNotesView.as_view(),
        name="evpnattachmentpoint_notes",
        kwargs={"model": models.EVPNAttachmentPoint},
    ),
    # EVPNEthernetSegment
    path("evpnethernetsegment/", views.EVPNEthernetSegmentListView.as_view(), name="evpnethernetsegment_list"),
    path(
        "evpnethernetsegment/add/",
        views.EVPNEthernetSegmentEditView.as_view(),
        name="evpnethernetsegment_add",
    ),
    path(
        "evpnethernetsegment/edit/",
        views.EVPNEthernetSegmentBulkEditView.as_view(),
        name="evpnethernetsegment_bulk_edit",
    ),
    path(
        "evpnethernetsegment/delete/",
        views.EVPNEthernetSegmentBulkDeleteView.as_view(),
        name="evpnethernetsegment_bulk_delete",
    ),
    path(
        "evpnethernetsegment/<uuid:pk>/",
        views.EVPNEthernetSegmentDetailView.as_view(),
        name="evpnethernetsegment",
    ),
    path(
        "evpnethernetsegment/<uuid:pk>/edit/",
        views.EVPNEthernetSegmentEditView.as_view(),
        name="evpnethernetsegment_edit",
    ),
    path(
        "evpnethernetsegment/<uuid:pk>/delete/",
        views.EVPNEthernetSegmentDeleteView.as_view(),
        name="evpnethernetsegment_delete",
    ),
    path(
        "evpnethernetsegment/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="evpnethernetsegment_changelog",
        kwargs={"model": models.EVPNEthernetSegment},
    ),
    path(
        "evpnethernetsegment/<uuid:pk>/notes/",
        ObjectNotesView.as_view(),
        name="evpnethernetsegment_notes",
        kwargs={"model": models.EVPNEthernetSegment},
    ),
    # EVPNEthernetSegmentLAGInterface
    path(
        "evpnesilaginterface/",
        views.EVPNEthernetSegmentLAGInterfaceListView.as_view(),
        name="evpnethernetsegmentlaginterface_list",
    ),
    path(
        "evpnesilaginterface/add/",
        views.EVPNEthernetSegmentLAGInterfaceEditView.as_view(),
        name="evpnethernetsegmentlaginterface_add",
    ),
    path(
        "evpnesilaginterface/edit/",
        views.EVPNEthernetSegmentLAGInterfaceBulkEditView.as_view(),
        name="evpnethernetsegmentlaginterface_bulk_edit",
    ),
    path(
        "evpnesilaginterface/delete/",
        views.EVPNEthernetSegmentLAGInterfaceBulkDeleteView.as_view(),
        name="evpnethernetsegmentlaginterface_bulk_delete",
    ),
    path(
        "evpnesilaginterface/<uuid:pk>/",
        views.EVPNEthernetSegmentLAGInterfaceDetailView.as_view(),
        name="evpnethernetsegmentlaginterface",
    ),
    path(
        "evpnesilaginterface/<uuid:pk>/edit/",
        views.EVPNEthernetSegmentLAGInterfaceEditView.as_view(),
        name="evpnethernetsegmentlaginterface_edit",
    ),
    path(
        "evpnesilaginterface/<uuid:pk>/delete/",
        views.EVPNEthernetSegmentLAGInterfaceDeleteView.as_view(),
        name="evpnethernetsegmentlaginterface_delete",
    ),
    path(
        "evpnesilaginterface/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="evpnethernetsegmentlaginterface_changelog",
        kwargs={"model": models.EVPNEthernetSegmentLAGInterface},
    ),
    path(
        "evpnesilaginterface/<uuid:pk>/notes/",
        ObjectNotesView.as_view(),
        name="evpnethernetsegmentlaginterface_notes",
        kwargs={"model": models.EVPNEthernetSegmentLAGInterface},
    ),
]
