# Create your views here.
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext

def index(request):
    template = 'index.html'
    data = {}
    print 'home'
    return render_to_response(template,data,context_instance = RequestContext(request))