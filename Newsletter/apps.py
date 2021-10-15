from django.apps import AppConfig

from .settings import set_settings


class NewsletterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Newsletter'

    def ready(self):
        from .schedule import delete_not_confirmed_members_schedule
        set_settings()
        delete_not_confirmed_members_schedule()
