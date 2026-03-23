from django.urls import path, re_path
from pretalx.event.models.event import SLUG_REGEX

from . import views
from .views import SingleSignOnSettingsView

urlpatterns = [
    re_path(
        rf"^orga/event/(?P<event>{SLUG_REGEX})/settings/p/sso/$",
        SingleSignOnSettingsView.as_view(),
        name="settings",
    ),
    # authentication / association
    path("p/sso/login/<str:backend>/", views.auth, name="begin"),
    path("p/sso/complete/<str:backend>/", views.complete, name="complete"),
    # disconnection
    path(
        "p/sso/disconnect/<str:backend>/",
        views.disconnect,
        name="disconnect",
    ),
    path(
        "p/sso/disconnect/<str:backend>/<int:association_id>/",
        views.disconnect,
        name="disconnect_individual",
    ),
]
