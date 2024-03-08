
from django.contrib import admin
from django.urls import path, include
from travelproject import settings


from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('travelapp.urls')),
    path('credentials/', include('credentials.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

