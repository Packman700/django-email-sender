from django import template
from django.conf import settings
from django.urls import reverse

from django.core.exceptions import ImproperlyConfigured

register = template.Library()

@register.simple_tag(name="full_url")
def get_full_url(input_url, *args):
    try:
        # THIS ISN'T TESTED BECAUSE RIGHT NOW IDK HOW DOMAINS WORKS :p
        from django.contrib.sites.models import Site
        current_site = Site.objects.get_current()
        url_domain = current_site.domain
    except (ImproperlyConfigured, RuntimeError):
        url_domain = settings.LOCAL_HOST_NAME
        url_directory = reverse(input_url, args=args)

    return "http://" + url_domain + url_directory
