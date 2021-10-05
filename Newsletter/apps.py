from django.apps import AppConfig
from .settings import set_settings

# To use this app you need add your server ip or domain to settings.ALLOWED_HOSTS
class NewsletterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Newsletter'

    def ready(self):
        set_settings()
