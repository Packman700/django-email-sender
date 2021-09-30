from django.test import TestCase, Client
from django.urls import reverse, resolve
# from ..views import JoinNewsletter, JoinNewsletterSuccess
from ..models import Member

class TestJoinNewsletter(TestCase):
    def setUp(self):
        self.join_url = reverse("newsletter:join-newsletter")
        self.join_template = "join_newsletter.html"
        self.success_url = reverse("newsletter:join-newsletter-success", kwargs={'id': 1})
        # self.success_template = "join_newsletter_success.html"
        self.client = Client()

    # Join
    def test_join_status_and_template_GET(self):
        response = self.client.get(self.join_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.join_template)

    def test_join_status_and_template_POST_valid_data(self):
        response = self.client.post(self.join_url, {
            'email': "test_mail@gmail.com",
            'confirmed': False,
            'name': "Test name 1"
        })
        # Test code
        self.assertEqual(response.status_code, 302)

        # Test success url
        # Take everything before last '/' in url (including '/')
        url_prefix = str(self.success_url)[:str(self.success_url).rfind('/')+1]
        self.assertRegex(response.url, f"{url_prefix}[0-9]+")

        # Test saving data
        new_object_id = int(response.url.lstrip(url_prefix))
        new_object = Member.objects.get(id=new_object_id)
        self.assertEqual(new_object.email, "test_mail@gmail.com")
        self.assertEqual(new_object.confirmed, False)
        self.assertEqual(new_object.name, "Test name 1")

    def test_join_status_and_template_POST_no_data(self):
        response = self.client.post(self.join_url)
        # Test code
        self.assertEqual(response.status_code, 200)
        # Test saving data
        self.assertEqual(Member.objects.count(), 0)

    def test_join_status_and_template_POST_invalid_data(self):
        response = self.client.post(self.join_url, {
            'email': "bad_mail.gmail.com",
            'name': "Test name 1"
        })
        # Test code
        self.assertEqual(response.status_code, 200)
        # Test saving data
        self.assertEqual(Member.objects.count(), 0)



class TestJoinNewsletterSuccess(TestCase):
    def setUp(self):
        self.success_url = reverse("newsletter:join-newsletter-success", kwargs={'id': 1})
        self.success_template = "join_newsletter_success.html"

        self.client = Client()

    # Success join
    def test_success_join_status_and_template_GET_success(self):
        Member.objects.create(
            email="test_mail@gmail.com",
            confirmed=False,
            name="Test name 1",
        )
        response = self.client.get(self.success_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.success_template)

    def test_success_join_status_and_template_GET_no_data(self):
        response = self.client.get(self.success_url)
        self.assertEqual(response.status_code, 404)


