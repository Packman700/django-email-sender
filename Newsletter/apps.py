from django.apps import AppConfig
from django.conf import settings
from .settings import set_settings

class NewsletterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Newsletter'

    def ready(self):
        set_settings()
        print(getattr(settings, "EMAIL_HOST_USER"))
