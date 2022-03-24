from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path


admin.site.site_header = "E-Health Admin"
admin.site.site_title = "E-Health Admin"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("hms.urls")),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
