from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from cinkeate.apps.home.models import Materia, Usuario, Programa
from django.contrib.auth.models import User

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





# Controlador de registro de usuario
def register_view(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			usuario = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["pass"])
			usuario.first_name = request.POST['nombre']
			usuario.last_name = request.POST['apellido']
			usuario.save()
			return HttpResponseRedirect('/home')
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')



#Controlador de vista de home *Vista de Perfil proximamente
def home_view(request):
	if request.method == 'POST':
		fecha = request.POST['fecha']
		semestre = request.POST['semestre']
		programa = request.POST['programa']
		telefono = request.POST['telefono']
		idPrograma = Programa.objects.get(nombre = programa)
		perfil = Usuario(user = request.user, fechaNacimiento = fecha, idPrograma = idPrograma, semestre = semestre, telefono = telefono )
		perfil.save()
		return HttpResponseRedirect('/home')
	else:
		if request.user.is_authenticated():
			try:
				if request.user.get_profile():
					return render_to_response('home.html', context_instance = RequestContext(request))	
			except:
				programas = Programa.objects.all()
				semestres = range(1,11)
				return render_to_response('datos.html',locals(),context_instance = RequestContext(request))
		else:
			return HttpResponseRedirect('/')

#inicio Darwin
def lista_materias(request):
	materias=Materia.objects.all()
	usuario = request.user
	perfil= Usuario.objects.get(user=usuario)
	inscripciones= perfil.materias.all()
	return render_to_response('semaforo.html', {'usuario':usuario, 'lista':materias, 'perfil':perfil, 'matInsc':inscripciones})
#fin Darwin