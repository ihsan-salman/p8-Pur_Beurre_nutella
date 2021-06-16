#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('mes_aliments/index.html')
    return HttpResponse(template.render(request=request))

def product(request):
    template = loader.get_template('mes_aliments/mes_produits.html')
    return HttpResponse(template.render(request=request))

def connexion(request):
    template = loader.get_template('mes_aliments/mon_compte.html')
    return HttpResponse(template.render(request=request))
