'''!/usr/bin/python3
   -*- coding: Utf-8 -'''

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from .models import Category, Product, Favorite, Contact
from .forms import RegisterForm

# Create your views here.

def index(request):
    template = loader.get_template('mes_aliments/index.html')
    return HttpResponse(template.render(request=request))

def product(request):
    template = loader.get_template('mes_aliments/mes_produits.html')
    if request.method == 'POST':
        search_request = request.POST.get('request_search')
        product_search = Product.objects.filter(name__icontains=search_request)
    url = 'https://fr.openfoodfacts.org/produit/3242272346050/dolce-pizza-prosciutto-sodebo'
    context =  {'products':product_search, 'url':url}
    return HttpResponse(template.render(context, request=request))

def create(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            name = request.POST.get('username')
            password = make_password(request.POST.get('password1'))
            contact = Contact.objects.filter(email=email)
            if not contact.exists():
                # If a contact is not registered, create a new one.
                user = User.objects.create(
                    username=name,
                    email=email,
                    password=password
                )
                user.save()
            else:
                contact = contact.first()

            return redirect('/')
        else:
            # Form data doesn't match the expected format.
            # Add errors to the template.
            context['errors'] = form.errors.items()
    else:
        form = RegisterForm()
    return render(request, 'registration/create.html', {'form':form})

def my_account(request):
    template = loader.get_template('mes_aliments/my_account.html')
    user = User.objects.get(name='')
    return HttpResponse(template.render(request=request))
