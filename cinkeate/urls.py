from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^',include('cinkeate.apps.home.urls')),
    url(r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)
