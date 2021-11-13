import sys

from django.apps import AppConfig
from django_newsletter.settings import set_settings


class DjangoNewsletterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_newsletter'

    def ready(self):
        set_settings()

        from .schedule import schedule_delete_not_confirmed_members
        from .signals import init_signals

        schedule_delete_not_confirmed_members()
        init_signals()
