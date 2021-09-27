from django.urls import path
from .views import JoinNewsletter

app_name = "newsletter"
urlpatterns = [
    path("join-newsletter/", JoinNewsletter.as_view(), name='join-newsletter'),
    path("join-newsletter/thanks/", JoinNewsletter.as_view(), name='join-newsletter-success'),
]
