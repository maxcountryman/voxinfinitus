from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def get_menulist():	
	return {'Home': '/', 'Discover': '/discover/', 'Services': '/services/', 'Participate': '/participate/'}

def landing(request):
	menulist = get_menulist()
	curview = 'Home'
	return render_to_response("index.html", locals(), context_instance=RequestContext(request))

def discover(request):
	menulist = get_menulist()
	curview = 'Discover'
	return render_to_response("discover.html", locals(), context_instance=RequestContext(request))

def services(request):
	menulist = get_menulist()
	curview = 'Services'
        return render_to_response("services.html", locals(), context_instance=RequestContext(request))

def participate(request):
	menulist = get_menulist()
	curview = 'Participate'
        return render_to_response("participate.html", locals(), context_instance=RequestContext(request))
