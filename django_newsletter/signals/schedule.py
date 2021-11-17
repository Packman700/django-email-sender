"""Here i modify default Schedule model behavior"""
from django.dispatch import receiver
from django_q.tasks import Schedule
from django.db.models.signals import pre_save
from croniter import croniter
from datetime import datetime


@receiver(pre_save, sender=Schedule)
def modify_cron_next_run_time(sender, instance, **kwargs):
    if instance.schedule_type == "C" and instance.cron and instance.pk is None:
        now = datetime.now()
        cron_schedule = instance.cron
        cron = croniter(cron_schedule, now)
        next_run = cron.get_next(datetime)
        instance.next_run = next_run
