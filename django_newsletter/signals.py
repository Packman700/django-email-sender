from django.db.models.signals import post_save, pre_delete
from django_newsletter.schedule import (schedule_mail_message_to_date, schedule_mail_message_cron)
from .models.email_message import EmailMessageToDate, EmailMessageCron


def mail_post_save(sender, instance, **kwargs):
    if sender is EmailMessageCron:
        schedule_mail_message_cron(instance, "SAVE")
    elif sender is EmailMessageToDate:
        schedule_mail_message_to_date(instance, "SAVE")


def mail_pre_delete(sender, instance, **kwargs):
    if sender is EmailMessageCron:
        schedule_mail_message_cron(instance, "DELETE")
    elif sender is EmailMessageToDate:
        schedule_mail_message_to_date(instance, "DELETE")


def init_signals():
    models = [EmailMessageToDate, EmailMessageCron]
    for model in models:
        post_save.connect(mail_post_save, sender=model)
        pre_delete.connect(mail_pre_delete, sender=model)
