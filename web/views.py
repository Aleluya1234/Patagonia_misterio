from django.shortcuts import render
import json, os
from django.conf import settings

def catalogo(request):
    ruta_json = os.path.join(settings.BASE_DIR, "datos.json")
    with open(ruta_json, encoding="utf-8") as f:
        misterios = json.load(f)
    return render(request, "catalogo.html", {"misterios": misterios})

def inicio(request):
    return render(request, "inicio.html", {"mensaje": "Explora los misterios de la Patagonia chilena"})

def nosotros(request):
    return render(request, "nosotros.html", {"equipo": "Grupo de estudiantes apasionados por la historia y las leyendas"})

def contacto(request):
    return render(request, "contacto.html", {"email": "contacto@patagonia-misterios.com"})

