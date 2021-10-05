from django.urls import path
from .views import (JoinNewsletter,
                    JoinNewsletterSuccess,
                    JoinNewsletterConfirm)

app_name = "newsletter"
urlpatterns = [
    path("join-newsletter/", JoinNewsletter.as_view(), name='join-newsletter'),
    path("join-newsletter/thanks/<int:id>", JoinNewsletterSuccess.as_view(), name='join-newsletter-success'),
    path("join-newsletter/confirm/<uuid:uuid>", JoinNewsletterConfirm.as_view(), name='confirm-join-newsletter'),

]
