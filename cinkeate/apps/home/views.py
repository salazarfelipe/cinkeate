from django.shortcuts import render_to_response
from django.template import RequestContext
from cinkeate.apps.home.models import Materia


def index_view(request):
	contenido = "este es el contenido de la pagina"
	materias = Materia.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request) )