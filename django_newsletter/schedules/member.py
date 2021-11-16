from django_q.tasks import Schedule
from datetime import datetime

ROOT_PACKAGE = __package__.split(".")[0]


def schedule_delete_not_confirmed_members(name="Delete not confirmed members",
                                          func=f'{ROOT_PACKAGE}.models.member.Member.delete_not_confirm_members'):
    """Schedule deletion not confirmed members"""
    if obj := Schedule.objects.filter(func=func, name=name):
        obj.delete()

    Schedule.objects.create(func=func, name=name, schedule_type="C", cron="0 0 * * *", next_run=datetime.now())


def schedule_delete_confirmed_members(name="Delete not confirmed members",
                                      func=f'{ROOT_PACKAGE}.models.member.Member.delete_confirm_members'):
    """Schedule deletion not confirmed members"""
    if obj := Schedule.objects.filter(func=func, name=name):
        obj.delete()

    Schedule.objects.create(func=func, name=name, schedule_type="C", cron="0 0 * * *", next_run=datetime.now())
