import uuid
from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone

from django_newsletter.mail_factory import welcome_mail


class Member(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    confirmed = models.BooleanField(default=False)
    username = models.CharField(max_length=50)
    join_datetime = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.id} {self.email}"

    @classmethod
    def delete_not_confirm_members(cls):
        """Function delete all not confirmed accounts
        after two days email no confirmation
        """
        countdown_days = settings.AFTER_HOW_MANY_DAYS_DELETE_USER
        objects = cls.objects.filter(confirmed=False,
                                     join_datetime__lte=timezone.now() - timedelta(days=countdown_days))
        objects.delete()

    @classmethod
    def delete_confirm_members(cls):
        """Function delete all not confirmed accounts
        after two days email no confirmation
        """
        countdown_days = 2
        objects = cls.objects.filter(confirmed=True,
                                     join_datetime__lte=timezone.now() - timedelta(days=countdown_days))
        objects.delete()

    def send_welcome_mail(self):
        title = settings.WELCOME_MAIL_TITLE
        sender_email = settings.EMAIL_HOST_USER
        recipient_email = self.email

        email_content = welcome_mail(uuid, self)

        send_mail(title, "", sender_email, [recipient_email], html_message=email_content)
