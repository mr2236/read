
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include(('medium.core.urls', 'core'), namespace='core')),
    path('leis/', include(('medium.leis.urls', 'leis'), namespace='leis')),
    path('conta/', include(('medium.accounts.urls', 'accounts'), namespace='accounts')),
    path('admin/', admin.site.urls),
    #path('api/', include(api_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)