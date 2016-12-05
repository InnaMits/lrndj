"""
WSGI config for learnpydjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys


#path = '/home/vm/learnpy/learnpydjango'
#if path not in sys.path:
 #   sys.path.append(path)

#os.environ['DJANGO_SETTINGS_MODULE'] =

from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learnpydjango.settings")

application = get_wsgi_application()
