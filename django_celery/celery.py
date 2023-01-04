import os

from celery import Celery
from django.apps import apps

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery.settings")
app = Celery("django_celery")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
