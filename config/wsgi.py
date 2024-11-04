"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Define a variável de ambiente padrão para as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Obtenha a aplicação WSGI para ser usada pelo servidor
application = get_wsgi_application()
