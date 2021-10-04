from django import template
from django.conf import settings
from django.urls import reverse

register = template.Library()

@register.simple_tag(name="full_url")
def get_full_url(input_url, *args):
    url_domain = settings.ALLOWED_HOSTS[0] if len(settings.ALLOWED_HOSTS) else "127.0.0.1:8000"
    url_directory = reverse(input_url, args=args)
    return "http://" + url_domain + url_directory
