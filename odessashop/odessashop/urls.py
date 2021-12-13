from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from odessashop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/shop/', include('apps.shop.urls')),
    path('api/', include('rest_framework.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
