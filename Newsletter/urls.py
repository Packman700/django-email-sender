from django.urls import path
from .views import JoinNewsletter, JoinNewsletterSuccess
from .mail_factory import JoinNewsletterWelcomeMail

app_name = "newsletter"
urlpatterns = [
    path("join-newsletter/", JoinNewsletter.as_view(), name='join-newsletter'),
    path("join-newsletter/confirm", JoinNewsletter.as_view(), name='confirm-join-newsletter'),
    path("join-newsletter/thanks/<int:id>", JoinNewsletterSuccess.as_view(), name='join-newsletter-success'),

    path("mail/welcome-mail/<uuid:uuid>", JoinNewsletterWelcomeMail.as_view(), name='welcome-mail'),
]
