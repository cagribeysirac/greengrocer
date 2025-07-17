import os

from django.apps import AppConfig


class CustomAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"

    path = os.path.dirname(__file__)
    name = ".".join(os.path.abspath(path).split(os.sep)[-3:])
