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
    if request.method == 'POST':
        product_id = request.POST.get('pk_prod')
        substitute_id = request.POST.get('pk_subs')
        favorite_registered = Favorite.objects.filter(
            product_id=product_id, substitute_id=substitute_id)
        if not favorite_registered.exists():
            username = request.user.username
            favorite = Favorite.objects.create(
                product_id=product_id,
                substitute_id=substitute_id,
                username=username)
            favorite.save()
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
    my_product_nutriscore = my_product.nutriscore_grade
    if my_product_nutriscore == 'e':
        list_score = ["d", "c", "b", "a"]
        substitute_search = Product.objects.filter(
            category_id=my_product.category_id).filter(
            nutriscore_grade__in=list_score).exclude(
            id=my_product.id)
    elif my_product_nutriscore == 'd':
        list_score = ["c", "b", "a"]
        substitute_search = Product.objects.filter(
            nutriscore_grade__in=list_score).filter(
            category_id=my_product.category_id).exclude(
            id=my_product.id)
    elif my_product_nutriscore == 'c':
        list_score = ["c", "b", "a"]
        substitute_search = Product.objects.filter(
            nutriscore_grade__in=list_score).filter(
            category_id=my_product.category_id).exclude(
            id=my_product.id)
    elif my_product_nutriscore == 'b':
        list_score = ["b", "a"]
        substitute_search = Product.objects.filter(
            nutriscore_grade__in=list_score).filter(
            category_id=my_product.category_id).exclude(
            id=my_product.id)
    else:
        list_score = ["a"]
        substitute_search = Product.objects.filter(
            nutriscore_grade__in=list_score).filter(
            category_id=my_product.category_id).exclude(
            id=my_product.id)
    context = {'product': my_product,
               'substitutes': substitute_search,}
    return HttpResponse(template.render(context, request=request))

def detail_product(request, pk):
    '''get the pk of the product and return the detail of the product'''
    template = loader.get_template('mes_aliments/mon_produit.html')
    if request.method == 'GET':
        product_search = Product.objects.filter(id=pk)
    context = {'product': product_search[0]}
    return HttpResponse(template.render(context, request=request))

def my_favorite(request):
    '''return the template of the favorites'''
    favorite_product = []
    favorite_substitute = []
    template = loader.get_template('mes_aliments/mes_favoris.html')
    if request.method == 'GET':
        favorites = Favorite.objects.filter(username=request.user.username)
        for favorite in favorites:
            product = Product.objects.filter(id=favorite.product_id)
            favorite_product.append(product[0])
            substitute = Product.objects.filter(id=favorite.substitute_id)
            favorite_substitute.append(substitute[0])
    context = {'favorite_product': favorite_product,
               'favorite_substitute': favorite_substitute}
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
                contact = Contact.objects.create(email=email, name=name)
                user.save()
                contact.save()
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
