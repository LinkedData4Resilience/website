from django.shortcuts import render
from .models import Greeting
# from django.http import HttpResponse
# Create your views here.
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def data(request):
    template = loader.get_template('data.html')
    context = {}
    return HttpResponse(template.render(context, request))


def publication(request):
    template = loader.get_template('publication.html')
    context = {}
    return HttpResponse(template.render(context, request))
