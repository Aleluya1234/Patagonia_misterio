from django.shortcuts import render
import json

def inicio(request):
    return render(request, "inicio.html")

def nosotros(request):
    return render(request, "nosotros.html")

def contacto(request):
    return render(request, "contacto.html")

def catalogo(request):
    with open("datos.json", encoding="utf-8") as f:
        misterios = json.load(f)
    return render(request, "catalogo.html", {"misterios": misterios})
