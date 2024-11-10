"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.views.static import serve

from proj.swagger import schema_view


class Redirect(RedirectView):
    pattern_name = 'schema-swagger-ui'

urlpatterns = [
    path('', Redirect.as_view(),name='home'),
    path('admin/', admin.site.urls),
    path('tech/', include('app.urls')),
    path('user/', include('users.urls')),
    path('comments/', include('avangers.urls')),
    path('application/', include('avangers.applications_urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('^media/(?P<path>.*)$',serve, {'document_root': settings.MEDIA_ROOT})
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)