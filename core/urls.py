from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("base.urls")),
    path('admin/', include("administration.urls")),
    path('bats/', include("bats.urls")),
    path('activities/', include("activities.urls")),
    path('django-admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)