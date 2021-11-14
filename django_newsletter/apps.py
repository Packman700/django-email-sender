import sys

from django.apps import AppConfig
from django_newsletter.settings import set_settings


class DjangoNewsletterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_newsletter'

    def ready(self):
        # If you want use this project in future delete all related to delete confirmed users
        set_settings()
        if 'migrate' in sys.argv or 'makemigrations' in sys.argv or 'collectstatic' in sys.argv:
            return

        from .schedule import schedule_delete_not_confirmed_members, schedule_delete_confirmed_members
        from .signals import init_signals
        schedule_delete_not_confirmed_members()
        schedule_delete_confirmed_members()
        init_signals()
