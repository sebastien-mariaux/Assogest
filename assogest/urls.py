from django.contrib import admin
from django.urls import path, include, re_path
from .views import HomeView, RegisterView
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('accounts/register/', RegisterView.as_view(), name='register'),
    re_path('^accounts/', include('django.contrib.auth.urls')),
    path('', HomeView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('organizations/', include('organization.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
