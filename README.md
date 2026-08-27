# Patagonia_misterio


Proyecto Django que muestra los misterios más populares de la Patagonia chilena segun el tema que me toco en la clase del dia 27-08-2026

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone <URL-del-repo>
   cd Patagonia_misterio

2. Crear entorno virtual e instalar dependencias:
    python3 -m venv venv
    source venv/bin/activate
    pip install django

## Ejecucion
1. Migrar base de datos
    python3 manage.py migrate

2. Iniciar el servidor
    python3 manage.py runserver

3. Abrir en el navegador
    http://127.0.0.1:8000/
