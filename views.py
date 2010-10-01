from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def get_menulist():	
	return {'Home': '/', 'Discover': '/discover/', 'Services': '/services/', 'Participate': '/participate/'}

def landing(request):
	menulist = get_menulist()
	curview = 'Home'
	return render_to_response("index.html", locals(), context_instance=RequestContext(request))
