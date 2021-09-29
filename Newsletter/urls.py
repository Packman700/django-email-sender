from django.urls import path
from .views import JoinNewsletter, JoinNewsletterSuccess

app_name = "newsletter"
urlpatterns = [
    path("join-newsletter/", JoinNewsletter.as_view(), name='join-newsletter'),
    path("join-newsletter/thanks/<int:id>", JoinNewsletterSuccess.as_view(), name='join-newsletter-success'),
]
