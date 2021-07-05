'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


from django.http import HttpResponse
from django.shortcuts import render, redirect  # , get_object_or_404
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .helper.functions import parse_request

from .models import Category, Product, Favorite, Contact
from .forms import RegisterForm


def index(request):
    '''return index template'''
    template = loader.get_template('mes_aliments/index.html')
    return HttpResponse(template.render(request=request))


def product(request):
    '''get the user's query and return the related product'''
    substitutes_image = []
    substitutes_nutriscore = []
    template = loader.get_template('mes_aliments/mes_produits.html')
    if request.method == 'POST':
        search_request = request.POST.get('request_search')
        product_search = Product.objects.filter(
            name__icontains=search_request)
    my_product = product_search[0]
    my_product_nutriscore = parse_request(my_product.nutriscore_grade)
    if my_product_nutriscore == 'e':
        list_score = ["('d',)", "('c',)", "('b',)", "('a',)"]
        substitute_search = Product.objects.filter(
            category_id=my_product.category_id).filter(
            nutriscore_grade__in=list_score).exclude(
            id=my_product.id)
    elif my_product_nutriscore == 'd':
        list_score = ["('c',)", "('b',)", "('a',)"]
        substitute_search = Product.objects.filter(
            nutriscore_grade__in=list_score).filter(
            category_id=my_product.category_id).exclude(
            id=my_product.id)
    elif my_product_nutriscore == 'c':
        list_score = ["('c',)", "('b',)", "('a',)"]
        substitute_search = Product.objects.filter(
            nutriscore_grade__in=list_score).filter(
            category_id=my_product.category_id).exclude(
            id=my_product.id)
    elif my_product_nutriscore == 'b':
        list_score = ["('b',)", "('a',)"]
        substitute_search = Product.objects.filter(
            nutriscore_grade__in=list_score).filter(
            category_id=my_product.category_id).exclude(
            id=my_product.id)
    else:
        list_score = ["('a',)"]
        substitute_search = Product.objects.filter(
            nutriscore_grade__in=list_score).filter(
            category_id=my_product.category_id).exclude(
            id=my_product.id)
    product_img = parse_request(my_product.image)
    product_nutriscore = parse_request(my_product.nutriscore_grade)
    for data in substitute_search:
        parsed_nutriscore_data = parse_request(data.nutriscore_grade)
        substitutes_nutriscore.append(parsed_nutriscore_data)
        parsed_img_data = parse_request(data.image)
        substitutes_image.append(parsed_img_data)
    context = {'product': my_product,
               'product_url': product_img,
               'substitutes': substitute_search,
               'substitutes_nutriscore':substitutes_nutriscore,
               'substitutes_image': substitutes_image}
    return HttpResponse(template.render(context, request=request))


def detail_product(request, pk):
    '''get the pk of the product and return the detail of the product'''
    product_image = []
    template = loader.get_template('mes_aliments/mon_produit.html')
    if request.method == 'GET':
        product_search = Product.objects.filter(id=pk)
    for data in product_search:
        parsed_image_data = parse_request(data.image)
        product_image.append(parsed_image_data)
        parsed_nutriscore_data = parse_request(data.nutriscore_grade)
        parsed_url = parse_request(data.url)
    context = {'product': product_search,
               'image_url': product_image,
               'nutriscore': parsed_nutriscore_data,
               'product_url': parsed_url}
    return HttpResponse(template.render(context, request=request))


def create(request):
    '''return the template to create an user account
       and add in the database all related information'''
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
    return render(request, 'registration/create.html', {'form': form})


def my_account(request):
    '''return the template of user's personal informations'''
    template = loader.get_template('mes_aliments/my_account.html')
    return HttpResponse(template.render(request=request))
