import sys

import django.db.models.options as options
from django.conf import settings
from django.core.mail import send_mail
from django.db import models

import django_newsletter.schedule as schedule
from django_newsletter.mail_factory import default_mail
from django_newsletter.models.member import Member

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('class_name', 'schedule_function_name')


class EmailMessageAbstract(models.Model):
    class Meta:
        abstract = True
        class_name = "EmailMessageAbstract"
        schedule_function_name = "schedule_abstract_mail_message"

    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.id} {self.title}"

    # Add abstraction to this
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        class_instance = self.__get_class_instance()
        schedule_function_name = self._meta.schedule_function_name

        if getattr(class_instance, "objects").filter(id=self.id):
            getattr(schedule, schedule_function_name)(self.pk, 'UPDATE', self.send_time)
        else:
            getattr(schedule, schedule_function_name)(self.pk, 'INSERT', self.send_time)

    def delete(self, *args, **kwargs):
        schedule_function_name = self._meta.schedule_function_name
        getattr(schedule, schedule_function_name)(self.pk, 'DELETE', self.send_time)
        super().delete(*args, **kwargs)

    def __get_class_instance(self):
        return getattr(sys.modules[__name__], self._meta.class_name)


class EmailMessageToDate(EmailMessageAbstract):
    class Meta:
        class_name = "EmailMessageToDate"
        schedule_function_name = "schedule_mail_message_to_date"

    send_time = models.DateTimeField()
    is_send = models.BooleanField(default=False)

    @classmethod
    def send_mail_to_all_members(cls, id_):
        """Sending mail to all members"""
        members_objects = Member.objects.filter(confirmed=True)

        mail = cls.objects.filter(id=id_)
        mail.update(is_send=True)
        mail = mail.first()

        sender_email = settings.EMAIL_HOST_USER
        members_mails = [member.email for member in members_objects]
        email_content = default_mail(mail.content)

        send_mail(mail.title, "", sender_email, members_mails, html_message=email_content)

# class EmailMessageCron(EmailMessage):
