#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


from .models import Category, Product, Favorite, Contact
from .forms import RegisterForm

# Create your views here.

def index(request):
    template = loader.get_template('mes_aliments/index.html')
    return HttpResponse(template.render(request=request))

def product(request):
    template = loader.get_template('mes_aliments/mes_produits.html')
    return HttpResponse(template.render(request=request))

def create(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            contact = Contact.objects.filter(email=email)
            if not contact.exists():
                # If a contact is not registered, create a new one.
                contact = Contact.objects.create(
                    email=email,
                    name=name,
                    password=password
                )
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
