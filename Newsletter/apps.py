from django.apps import AppConfig

from .settings import set_settings


class NewsletterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Newsletter'

    def ready(self):
        from .schedule import schedule_tasks
        set_settings()
        schedule_tasks()
