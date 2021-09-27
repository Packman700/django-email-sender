from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import JoinNewsletter

class TestUrls(SimpleTestCase):
    def test_join_newsletter_url(self):
        url = reverse('newsletter:join-newsletter')
        self.assertEquals(JoinNewsletter, resolve(url).func.view_class)

