from django.urls import path
from nautobot.extras.views import ObjectChangeLogView, ObjectNotesView
from nautobot_plugin_evpn import models, views

app_name = "evpn"

urlpatterns = [
    # EVPNService
    path("evpn-service/", views.EVPNServiceListView.as_view(), name="evpnservice_list"),
    path(
        "evpn-service/add/",
        views.EVPNServiceEditView.as_view(),
        name="evpnservice_add",
    ),
    path(
        "evpn-service/edit/",
        views.EVPNServiceBulkEditView.as_view(),
        name="evpnservice_bulk_edit",
    ),
    path(
        "evpn-service/delete/",
        views.EVPNServiceBulkDeleteView.as_view(),
        name="evpnservice_bulk_delete",
    ),
    path(
        "evpn-service/<uuid:pk>/",
        views.EVPNServiceDetailView.as_view(),
        name="evpn-service",
    ),
    path(
        "evpn-service/<uuid:pk>/edit/",
        views.EVPNServiceEditView.as_view(),
        name="evpnservice_edit",
    ),
    path(
        "evpn-service/<uuid:pk>/delete/",
        views.EVPNServiceDeleteView.as_view(),
        name="evpnservice_delete",
    ),
    path(
        "evpn-service/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="evpnservice_changelog",
        kwargs={"model": models.EVPNService},
    ),
    path(
        "evpn-service/<uuid:pk>/notes/",
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
    path("evpn-layer2-vrf/", views.EVPNLayer2VRFListView.as_view(), name="evpn-layer2-vrf_list"),
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
]
