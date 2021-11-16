from .member import (schedule_delete_not_confirmed_members,
                     schedule_delete_confirmed_members)


def init_schedules():
    schedule_delete_confirmed_members()
    schedule_delete_confirmed_members()