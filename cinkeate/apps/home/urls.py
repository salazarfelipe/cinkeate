<<<<<<< HEAD
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('cinkeate.apps.home.views',
		url(r'^$','index_view', name='vistaPrincipal'),
	)
=======
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('cinkeate.apps.home.views',
    url(r'^$', 'index_view', name='vistaPrincipal'),
)
>>>>>>> e7171b4962b67417526872639f274922f8dcca15
