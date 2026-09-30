import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("{{ cookiecutter.project_slug }}")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(["{{ cookiecutter.app_name }}.tasks"])
