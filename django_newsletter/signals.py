from django.db.models.signals import post_save, pre_delete, pre_save

from django_newsletter.schedule import (schedule_mail_message_to_date,
                                        schedule_mail_message_cron,
                                        schedule_mail_message_membership_time)
from .models.email_message import (EmailMessageToDate,
                                   EmailMessageCron,
                                   EmailMessageMembershipTime)


def mail_post_save(sender, instance, **kwargs):
    if sender is EmailMessageCron:
        schedule_mail_message_cron(instance, "SAVE")
    elif sender is EmailMessageToDate:
        schedule_mail_message_to_date(instance, "SAVE")
    elif sender is EmailMessageMembershipTime:
        schedule_mail_message_membership_time(instance, "SAVE")


def mail_pre_delete(sender, instance, **kwargs):
    if sender is EmailMessageCron:
        schedule_mail_message_cron(instance, "DELETE")
    elif sender is EmailMessageToDate:
        schedule_mail_message_to_date(instance, "DELETE")
    elif sender is EmailMessageMembershipTime:
        schedule_mail_message_membership_time(instance, "DELETE")


def mail_pre_save(sender, instance, **kwargs):
    if not instance.database_title:
        instance.database_title = instance.title


def init_signals():
    models = [EmailMessageToDate, EmailMessageCron, EmailMessageMembershipTime]
    for model in models:
        post_save.connect(mail_post_save, sender=model)
        pre_delete.connect(mail_pre_delete, sender=model)
        pre_save.connect(mail_pre_save, sender=model)
