from django_q.tasks import Schedule

from .schedule_tools import prevent_multiple_schedule_in_one_day


def schedule_tasks():
    """Group all schedules"""
    delete_not_confirmed_members_schedule()


@prevent_multiple_schedule_in_one_day
def delete_not_confirmed_members_schedule(name="Delete not confirmed members",
                                          func=f'{__package__}.models.Member.delete_not_confirm_members'):
    """Schedule deletion not confirmed members"""
    Schedule.objects.create(func=func, name=name, schedule_type=Schedule.DAILY)
