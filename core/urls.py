"""URL configuration for core project."""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = []

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"v1/", include("server.apps.users.urls")),
    # path(r"v1/", include("server.apps.base.routers")),
    path(r"swagger/", include("server.apps.base.swagger")),
    # path("", TemplateView.as_view(template_name="index.html"), name="index"),
    # re_path(
    #     r"^(?:.*)/?$", TemplateView.as_view(template_name="index.html"), name="index"
    # ),
]
