from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def landing(request):
	return render_to_response("index.html", locals(), context_instance=RequestContext(request))
