from django.conf.urls import url
from django.urls import path
from django.conf.urls import url
from .views import JoinNewsletter

app_name = "newsletter"
urlpatterns = [
    # path("join-newsletter/", JoinNewsletter.as_view(), name='join-newsletter'),
    path("join-newsletter/thanks/", JoinNewsletter.as_view(), name='join-newsletter-success'),
    path("join-newsletter/", JoinNewsletter.as_view(), name='join-newsletter'),
    # url(r'^join-newsletter/(?P<success>\w+)$', JoinNewsletter.as_view(), name="join-newsletter"),

]
