from django.shortcuts import render
from .models import Greeting
# from django.http import HttpResponse
# Create your views here.
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext

from SPARQLWrapper import SPARQLWrapper, JSON

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def data(request):
    template = loader.get_template('data.html')
    context = {}
    return HttpResponse(template.render(context, request))



def integrated(request):
    template = loader.get_template('integrated.html')
    context = {}
    return HttpResponse(template.render(context, request))

def integratedevent(request, eventid):
    # template = loader.get_template('integratedevent.html')
    # context = {eventid}
    # return HttpResponse(template.render(context, request))
    print (eventid)
    msg = f'Event in the integrated dataset: {eventid}.'

    return HttpResponse(msg, content_type='text/plain')



def EOR(request):
    template = loader.get_template('EOR.html')
    context = {}
    return HttpResponse(template.render(context, request))


def EORevent(request, eventid):
    template = loader.get_template('EORevent.html')
    context = {'eventid': eventid}
    return HttpResponse(template.render(context, request))


def CH(request):
    template = loader.get_template('CH.html')
    context = {}
    return HttpResponse(template.render(context, request))


def CHevent(request, eventid):
    template = loader.get_template('CHevent.html')
    context = {'eventid': eventid}

    print ('working on the event ', eventid)


    sparql = SPARQLWrapper(
        "https://api.triplydb.com/datasets/linked4resilience/Civilian-Harm-April-2023/services/Civilian-Harm-April-2023/sparql"
    )
    sparql.setReturnFormat(JSON)

    result = ''

    # gets the first 3 geological ages
    # from a Geological Timescale database,
    # via a SPARQL endpoint
    sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX l4rCH: <https://linked4resilience.eu/data/CH/April2023/event/>
        SELECT * WHERE {
          l4rCH:00000001 ?pred ?obj .
        } LIMIT 10
        """
        # """ % { 'subj': 'https://linked4resilience.eu/data/CH/April2023/event/'+eventid }
    )

    try:
        ret = sparql.queryAndConvert()

        for r in ret["results"]["bindings"]:
            result += str(r)
    except Exception as e:
        print(e)

    context = {'eventid': eventid, 'result': result}

    return HttpResponse(template.render(context, request))
    # msg = f'Event in the CH dataset: {eventid}.'
    #
    # return HttpResponse(msg, content_type='text/plain')






def publication(request):
    template = loader.get_template('publication.html')
    context = {}
    return HttpResponse(template.render(context, request))
