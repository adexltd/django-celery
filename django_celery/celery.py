import os

from celery import Celery
from django.apps import apps
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery.settings")
app = Celery("django_celery")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(settings.INSTALLED_APPS)