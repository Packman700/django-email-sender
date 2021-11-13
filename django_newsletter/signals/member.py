from django.db.models.signals import post_save, pre_save

from django_newsletter.models.member import Member
from datetime import datetime


def member_post_save(sender, instance, created, **kwargs):
    if created:
        instance.send_welcome_mail()


def member_pre_save(sender, instance, **kwargs):
    instance.join_datetime = datetime.now()


def init_signals():
    post_save.connect(member_post_save, sender=Member)
    pre_save.connect(member_pre_save, sender=Member)
