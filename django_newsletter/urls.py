from django.urls import path
from django_newsletter.views import (JoinNewsletter,
                                     confirm_join_to_newsletter,
                                     delete_mail_from_newsletter)

app_name = "newsletter"
urlpatterns = [
    path("", JoinNewsletter.as_view(), name='join-newsletter'),
    path("join-newsletter/confirm/<uuid:uuid>", confirm_join_to_newsletter, name='confirm-join'),
    path("join-newsletter/delete/<uuid:uuid>", delete_mail_from_newsletter, name='delete-account'),
]
