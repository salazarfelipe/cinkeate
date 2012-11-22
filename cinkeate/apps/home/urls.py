from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('cinkeate.apps.home.views',
    url(r'^$', 'index_view', name='vistaPrincipal'),
)