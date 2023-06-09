import os, html, string, re
from django.shortcuts import render, HttpResponse, redirect, reverse
from .forms import ContactForm
from portafolioDB.models import Projects

def pagina_principal(request):
    template = 'index.html'
    return render(request, template)

def home_page(request):
    formulario_contacto = ContactForm
    projects = Projects.objects.filter(show=True)
    template = 'contact.html'
    if request.method == 'POST':
        formulario_contacto = formulario_contacto(data=request.POST)
        if formulario_contacto.is_valid():
            pass
            return redirect(reverse('home_page') + "?ok")
            
    return render(request, template, {'form': formulario_contacto, 'projects': projects})

def informacion_personal(request):
    template = 'about.html'
    return render(request, template)