from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from cinkeate.apps.home.models import Materia


def index_view(request):
	return render_to_response('index.html', locals(), context_instance = RequestContext(request) )

def login_view(request):
	try:
		username = request.POST['username']
		password = request.POST['password']
		usuario = authenticate(username=username, password=password)
		if usuario is not None and usuario.is_active:
			login(request, usuario)
			return HttpResponseRedirect('/admin')
	except:
		return HttpResponseRedirect('/')