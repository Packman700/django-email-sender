import sys

from django.apps import AppConfig

from django_newsletter.settings import set_settings


class DjangoNewsletterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_newsletter'

    def ready(self):
        set_settings()
        if 'runserver' in sys.argv:
            from .schedule import schedule_delete_not_confirmed_members
            schedule_delete_not_confirmed_members()
