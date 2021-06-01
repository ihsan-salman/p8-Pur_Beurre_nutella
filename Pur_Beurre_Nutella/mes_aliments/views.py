#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requests):
	message = 'salut tout le monde'
	return HttpResponse(message)