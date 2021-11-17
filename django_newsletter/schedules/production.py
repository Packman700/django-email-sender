from datetime import datetime

from django_q.tasks import Schedule

from django_newsletter.models.email_message import EmailMessageToDate

ROOT_PACKAGE = __package__.split(".")[0]


def create_and_delete_mail():
    obj = EmailMessageToDate.objects.create(send_time=datetime.now(), is_send=True, title="Prevent sleep",
                                            content="...", send_to_confirmed=False, send_to_not_confirmed=False)
    print("DZIAła")
    obj.delete()


def schedule_event_preventing_heroku_sleep(name="Prevent heroku sleep",
                                           func=f'{ROOT_PACKAGE}.schedules.production.create_and_delete_mail'):
    if obj := Schedule.objects.filter(func=func, name=name):
        obj.delete()

    Schedule.objects.create(func=func, name=name, schedule_type="C", cron="0,20,40 * * * *", next_run=datetime.now())
