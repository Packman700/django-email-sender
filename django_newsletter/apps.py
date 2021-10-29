import sys

from django.apps import AppConfig

from .settings import set_settings


class DjangoNewsletterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_newsletter'

    def ready(self):
        set_settings()
        if 'runserver' in sys.argv:
            from .schedule import delete_not_confirmed_members_schedule
            delete_not_confirmed_members_schedule()
