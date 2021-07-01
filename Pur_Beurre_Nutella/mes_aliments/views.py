'''!/usr/bin/python3
   -*- coding: Utf-8 -'''

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .helper.functions import parse_request

from .models import Category, Product, Favorite, Contact
from .forms import RegisterForm

# Create your views here.

def index(request):
    template = loader.get_template('mes_aliments/index.html')
    return HttpResponse(template.render(request=request))


def product(request):
    product_images = []
    template = loader.get_template('mes_aliments/mes_produits.html')
    if request.method == 'POST':
        search_request = request.POST.get('request_search')
        product_search = Product.objects.filter(name__icontains=search_request)
    for data in product_search:
        parsed_data = parse_request(data.image)
        product_images.append(parsed_data)
    context =  {'products':product_search, 'urls':product_images}
    return HttpResponse(template.render(context, request=request))


def detail_product(request, pk):
    product_image = []
    template = loader.get_template('mes_aliments/mon_produit.html')
    if request.method == 'GET':
        product_search = Product.objects.filter(id=pk)
    for data in product_search:
        parsed_image_data = parse_request(data.image)
        product_image.append(parsed_image_data)
        parsed_nutriscore_data = parse_request(data.nutriscore_grade)
        parsed_url = parse_request(data.url)
    context = {'product':product_search,
               'image_url':product_image,
               'nutriscore':parsed_nutriscore_data,
               'product_url': parsed_url}
    return HttpResponse(template.render(context, request=request))


def substitute(request, pk):
    template = loader.get_template('mes_aliments/mon_substitut.html')
    product_images = []
    products_nutriscore = []
    if request.method == 'GET':
        product_search = Product.objects.get(pk=pk)
    product_nutriscore = parse_request(product_search.nutriscore_grade)
    if product_nutriscore == 'e':
        list_score = ["('d',)","('c',)", "('b',)", "('a',)"]
        substitute_search = Product.objects.filter(category_id=product_search.category_id).filter(nutriscore_grade__in=list_score)
    elif product_nutriscore == 'd':
        list_score = ["('c',)", "('b',)", "('a',)"]
        substitute_search = Product.objects.filter(nutriscore_grade__in=list_score).filter(category_id=product_search.category_id)
    elif product_nutriscore == 'c':
        list_score = ["('c',)", "('b',)", "('a',)"]
        substitute_search = Product.objects.filter(nutriscore_grade__in=list_score).filter(category_id=product_search.category_id)
    elif product_nutriscore == 'b':
        list_score = ["('b',)", "('a',)"]
        substitute_search = Product.objects.filter(nutriscore_grade__in=list_score).filter(category_id=product_search.category_id)
    else:
        list_score = ["('a',)"]
        substitute_search = Product.objects.filter(nutriscore_grade__in=list_score).filter(category_id=product_search.category_id)
    for data in substitute_search:
        parsed_data = parse_request(data.image)
        product_images.append(parsed_data)
        parsed_nutriscore_data = parse_request(data.nutriscore_grade)
        products_nutriscore.append(parsed_nutriscore_data)
    context = {'substitute':substitute_search,
               'images_url':product_images,
               'nutriscores':products_nutriscore}
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
