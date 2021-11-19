"""Here i modify default Schedule model behavior"""
from datetime import datetime

from croniter import croniter
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_q.tasks import Schedule
import pytz


@receiver(pre_save, sender=Schedule)
def modify_cron_next_run_time(sender, instance, **kwargs):
    if instance.schedule_type == "C" and instance.cron and instance.pk is None:
        tz = pytz.timezone(settings.TIME_ZONE)
        aware_local_date = tz.localize(datetime.now())

        cron_schedule = instance.cron
        cron_obj = croniter(cron_schedule, aware_local_date)
        next_run = cron_obj.get_next(datetime)

        instance.next_run = next_run
