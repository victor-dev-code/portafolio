import os, html, string, re
from django.shortcuts import render, HttpResponse

def pagina_principal(request):
    template = 'index.html'
    return render(request, template)

def contacto(request):
    template = 'contact.html'
    return render(request, template)