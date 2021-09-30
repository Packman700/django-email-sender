from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import JoinNewsletter, JoinNewsletterSuccess

class TestUrls(SimpleTestCase):
    def test_join_newsletter_url(self):
        url = reverse('newsletter:join-newsletter')
        self.assertEquals(JoinNewsletter, resolve(url).func.view_class)

    def test_join_newsletter_success_url(self):
        url = reverse('newsletter:join-newsletter-success', kwargs={'id': 1})
        self.assertEquals(JoinNewsletterSuccess, resolve(url).func.view_class)

