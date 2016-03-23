# -*- coding: utf-8 -*-
from controlcenter.views import controlcenter
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/dashboard/', controlcenter.urls),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'', include('frontend.urls', namespace='frontend')),
    url(r'', include('digest.urls', namespace='digest')),
    url(r'', include('jobs.urls', namespace='jobs')),
    url(r'^likes/', include('likes.urls')),
    url(r'experiments/', include('experiments.urls')),
    # url(r"^account/", include('account.urls')),
    # url(r'', include('social.apps.django_app.urls', namespace='social'))

)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', url(r'^rosetta/', include('rosetta.urls')), )
