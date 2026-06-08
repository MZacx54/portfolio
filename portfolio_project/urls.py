from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    # SEO files served at root level
    path('robots.txt', TemplateView.as_view(
        template_name='robots.txt',
        content_type='text/plain'
    )),
    path('sitemap.xml', TemplateView.as_view(
        template_name='sitemap.xml',
        content_type='application/xml'
    )),
]

urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

