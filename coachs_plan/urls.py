from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('alt-admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('accounts/', include('allauth.urls')),
    path('plans/', include('plans.urls', namespace='plans')),
    path('blog/', include('blog.urls', namespace='blog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)