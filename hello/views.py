from django.shortcuts import render
from .models import Greeting
# from django.http import HttpResponse
# Create your views here.
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext

from SPARQLWrapper import SPARQLWrapper, JSON
import json

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

    context = {'eventid': eventid}

    sparql = SPARQLWrapper(
        "https://api.triplydb.com/datasets/linked4resilience/Civilian-Harm-April-2023/services/Civilian-Harm-April-2023/sparql"
    )
    sparql.setReturnFormat(JSON)

    resultJSON = ''

    # gets the first 3 geological ages
    # from a Geological Timescale database,
    # via a SPARQL endpoint
    sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX l4rCH: <https://linked4resilience.eu/data/CH/April2023/event/>
        SELECT * WHERE {
          l4rCH:"""
          + eventid +
          """ ?pred ?obj .
        } LIMIT 10
        """
    )

    try:
        ret = sparql.queryAndConvert()
        bindings = ret["results"]["bindings"]
        print ('original binding: ', bindings)

        context.update(decode_CH_SPARQL_binding(bindings))

    except Exception as e:
        print(e)

    print ('FINAL context: ', context)
    return HttpResponse(template.render(context, request))



def publication(request):
    template = loader.get_template('publication.html')
    context = {}
    return HttpResponse(template.render(context, request))

def use(request):
    template = loader.get_template('use.html')
    context = {}
    return HttpResponse(template.render(context, request))


def decode_CH_SPARQL_binding (bindings):
    # answer is the return string in JSON format by Triply.
    label = ''

    for b in bindings:
        if b['pred']['value'] == 'http://www.w3.org/2000/01/rdf-schema#label':
            label = b['obj']['value']
        if b['pred']['value'] == 'http://purl.org/dc/terms/date':
            date = b['obj']['value']
        if b['pred']['value']== 'https://linked4resilience.eu/ontology/addressCity':
            city = b['obj']['value']
        if b['pred']['value'] == 'https://schema.org/url':
            url = b['obj']['value']

    return {'label': label, 'date': date, 'city': city, 'url': url}





# {'head': {'link': [], 'vars': ['pred', 'obj']}, 'results': {'bindings': [{'pred': {'type': 'uri', 'value': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'}, 'obj': {'type': 'uri', 'value': 'http://semanticweb.cs.vu.nl/2009/11/sem/Event'}}, {'pred': {'type': 'uri', 'value': 'http://www.w3.org/2000/01/rdf-schema#label'}, 'obj': {'type': 'literal', 'value': 'civilian homes hit by artillery.'}}, {'pred': {'type': 'uri', 'value': 'http://purl.org/dc/terms/date'}, 'obj': {'type': 'literal', 'value': '2022-02-24', 'datatype': 'http://www.w3.org/2001/XMLSchema#date'}}, {'pred': {'type': 'uri', 'value': 'https://linked4resilience.eu/ontology/addressCity'}, 'obj': {'type': 'uri', 'value': 'http://sws.geonames.org/686946/'}}, {'pred': {'type': 'uri', 'value': 'https://linked4resilience.eu/ontology/addressCountry'}, 'obj': {'type': 'uri', 'value': 'http://sws.geonames.org/690791/'}}, {'pred': {'type': 'uri', 'value': 'https://linked4resilience.eu/ontology/addressRegion'}, 'obj': {'type': 'uri', 'value': 'http://sws.geonames.org/709716/'}}, {'pred': {'type': 'uri', 'value': 'https://schema.org/location'}, 'obj': {'type': 'uri', 'value': 'https://linked4resilience.eu/data/CH/April2023/location/00000006'}}, {'pred': {'type': 'uri', 'value': 'https://schema.org/postalCode'}, 'obj': {'type': 'literal', 'value': '87644'}}, {'pred': {'type': 'uri', 'value': 'https://schema.org/url'}, 'obj': {'type': 'literal', 'value': 'https://twitter.com/IntelCrab/status/1496840102651256832?s=20&t=vjuzVkVF9AjHtNtCWTtq9Q', 'datatype': 'http://www.w3.org/2001/XMLSchema#anyURI'}}]}}
