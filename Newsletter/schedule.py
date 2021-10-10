from datetime import datetime, timedelta

from django_q.tasks import Schedule


def schedule_tasks():
    """Group all schedules"""
    delete_not_confirmed_members_schedule()


def prevent_multiple_schedule_in_one_day(schedule_func):
    def decorator(func):
        """Decorator allow to create new schedule only if similar does not exist"""
        tomorrow = datetime.now() + timedelta(days=1)
        if not Schedule.objects.filter(
                func=schedule_func,
                next_run__year=tomorrow.year,
                next_run__month=tomorrow.month,
                next_run__day=tomorrow.day):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper
        return lambda: None

    return decorator


DELETE_NOT_CONFIRMED_MEMBERS_FUNC = f'{__package__}.models.Member.delete_not_confirm_members'
@prevent_multiple_schedule_in_one_day(schedule_func=DELETE_NOT_CONFIRMED_MEMBERS_FUNC)
def delete_not_confirmed_members_schedule():
    """Schedule deletion not confirmed members"""
    Schedule.objects.create(func=DELETE_NOT_CONFIRMED_MEMBERS_FUNC,
                            schedule_type=Schedule.DAILY
                            )
