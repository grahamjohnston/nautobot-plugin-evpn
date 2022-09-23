from django.urls import path
from nautobot.extras.views import ObjectChangeLogView, ObjectNotesView
from nautobot_plugin_evpn import models, views

app_name = "evpn"

urlpatterns = [
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
        name="examplemodel_notes",
        kwargs={"model": models.EVPNService},
    ),
]
