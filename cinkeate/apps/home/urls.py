from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('cinkeate.apps.home.views',
    url(r'^$', 'index_view', name='vistaPrincipal'),
    url(r'^login/$', 'login_view', name='vistaLogin'),
    url(r'^logout/$', 'logout_view', name='vistaLogout'),
    url(r'^registro/$','register_view',name="vista_registro"),
    url(r'^home/$', 'home_view', name='vistaHome'),
    url(r'^semaforo/$', 'lista_materias', name='vistaSemaforo'),
    url(r'^profile/$', 'profile_view', name='vistaPerfil'),
)