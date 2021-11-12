import sys

import django.db.models.options as options
from django.conf import settings
from django.core.mail import send_mail
from django.db import models

import django_newsletter.schedule as schedule
from django_newsletter.mail_factory import default_mail
from django_newsletter.models.member import Member

# from django_newsletter.schedule import schedule_mail_message_to_date
# from functools import partial
# from django.db.models.signals import post_save, pre_delete
# from django.dispatch import receiver

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

    #################
    # Create schedule
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        schedule_function_name = self._meta.schedule_function_name
        try:
            getattr(schedule, schedule_function_name)(self.pk, 'SAVE', self.send_time)
        except AttributeError:
            getattr(schedule, schedule_function_name)(self.pk, 'SAVE', self.cron)

    def delete(self, *args, **kwargs):
        schedule_function_name = self._meta.schedule_function_name
        try:
            getattr(schedule, schedule_function_name)(self.pk, 'DELETE', self.send_time)
        except AttributeError:
            getattr(schedule, schedule_function_name)(self.pk, 'DELETE', self.cron)
        super().delete(*args, **kwargs)
    #################

    @classmethod
    def send_mail_to_all_members(cls, id_, members=None):
        """Sending mail to all members"""
        if members is None:
            members_objects = Member.objects.filter(confirmed=True)
        else:
            members_objects = members

        mail = cls.objects.filter(id=id_).first()

        sender_email = settings.EMAIL_HOST_USER
        members_mails = [member.email for member in members_objects]
        email_content = default_mail(mail.content)

        send_mail(mail.title, "", sender_email, members_mails, html_message=email_content)

    def __get_class_instance(self):
        return getattr(sys.modules[__name__], self._meta.class_name)


class EmailMessageToDate(EmailMessageAbstract):
    class Meta:
        class_name = "EmailMessageToDate"
        schedule_function_name = "schedule_mail_message_to_date"

    send_time = models.DateTimeField()
    is_send = models.BooleanField(default=False)

    @classmethod
    def send_mail_to_all_members(cls, id_, members=None):
        """Sending mail to all members"""
        super(EmailMessageToDate).send_mail_to_all_members(id_)

        mail = cls.objects.filter(id=id_)
        mail.update(is_send=True)


class EmailMessageCron(EmailMessageAbstract):
    class Meta:
        class_name = "EmailMessageCron"
        schedule_function_name = "schedule_mail_message_cron"

    # TODO Add cron validator
    cron = models.CharField(max_length=30)


# # TODO ADD SIGNALS IN FUTURE
# MODELS_CALLBACK = [(EmailMessageToDate, schedule_mail_message_to_date)]
# for model, callback in MODELS_CALLBACK:
#     post_save.connect(receiver=partial(callback), sender=model, weak=False)
