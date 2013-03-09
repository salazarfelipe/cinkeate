from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from cinkeate.apps.home.models import Materia

# Controla el index o pagina inicial
# si no se ha iniciado sesion, renderuza la vista de index
# Si ya hay una sesion activa, determina que tipo de usuario es
# y lo envia a su respectiva vista
def index_view(request):
	if request.user.is_authenticated():
		if request.user.is_staff:
			return HttpResponseRedirect('/admin')
		else:
			return HttpResponseRedirect('/home')
	else:
		return render_to_response('index.html', locals(), context_instance = RequestContext(request) )



# controla el login de usuario
# Si es usuario administrador lo envia a la vista de admin
# si es usuario convencional lo envia al home (perfil de usuario)
def login_view(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
		usuario = authenticate(username=username, password=password)
		if usuario is not None and usuario.is_active:
			login(request, usuario)
			if usuario.is_staff:
				return HttpResponseRedirect('/admin')
			else:
				return HttpResponseRedirect('/home')

	except:
		return HttpResponseRedirect('/')
	loginFailed = True
	return render_to_response('index.html', locals(), context_instance = RequestContext(request) )



# Controlador del Cierre de Sesion
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')



#Controlador de vista de home *Vista de Perfil proximamente
def home_view(request):
	if request.user.is_authenticated():
		return render_to_response('home.html',locals(), context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/')