#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader


from .models import Category, Product, Favorite, Contact
from .forms import ContactForm

# Create your views here.

def index(request):
    template = loader.get_template('mes_aliments/index.html')
    return HttpResponse(template.render(request=request))

def product(request):
    template = loader.get_template('mes_aliments/mes_produits.html')
    return HttpResponse(template.render(request=request))

def connexion(request):
    template = loader.get_template('mes_aliments/mon_compte.html')
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

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
        else:
            # Form data doesn't match the expected format.
            # Add errors to the template.
            context['errors'] = form.errors.items()
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'mes_aliments/mon_compte.html', context)

