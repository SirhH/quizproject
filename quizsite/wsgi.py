import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quizsite.settings")

from whitenoice.django import DjangoWhiteNoice
application = DjangoWhiteNoice(get_wsgi_application())
