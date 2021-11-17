from .member import (schedule_delete_not_confirmed_members,
                     schedule_delete_confirmed_members)
from .production import schedule_event_preventing_heroku_sleep


def init_schedules():
    schedule_delete_confirmed_members()
    schedule_delete_confirmed_members()
    schedule_event_preventing_heroku_sleep()