import uuid
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django_newsletter.mail_factory import welcome_mail
from django.conf import settings
from django.db import models


class Member(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    confirmed = models.BooleanField(default=False)
    username = models.CharField(max_length=50)
    join_datetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.id} {self.email}"

    @classmethod
    def delete_not_confirm_members(cls):
        """Function delete all not confirmed accounts
        after two days email no confirmation
        """
        countdown_days = settings.AFTER_HOW_MANY_DAYS_DELETE_USER
        objects = cls.objects.filter(confirmed=False,
                                     join_datetime__lte=datetime.now() - timedelta(days=countdown_days))
        objects.delete()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.__send_welcome_mail()

    def __send_welcome_mail(self):
        title = settings.WELCOME_MAIL_TITLE
        sender_email = settings.EMAIL_HOST_USER
        recipient_email = self.email

        email_content = welcome_mail(uuid, self)

        send_mail(title, "", sender_email, [recipient_email], html_message=email_content)
