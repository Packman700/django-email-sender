""" File store all schedule create functions """

from django_q.tasks import Schedule
from django_newsletter.exceptions import (IdIsNotTypeIntError,
                                          InvalidMethodValueError)


def delete_not_confirmed_members_schedule(name="Delete not confirmed members",
                                          func=f'{__package__}.models.member.Member.delete_not_confirm_members'):
    """Schedule deletion not confirmed members"""
    if obj := Schedule.objects.filter(func=func, name=name):
        obj.delete()

    Schedule.objects.create(func=func, name=name, schedule_type=Schedule.DAILY)


def schedule_mail_message_to_date(id_, method, date,
                                  func=f"{__package__}.models.email_message.EmailMessageToDate.send_mail_to_all_members"):
    """Schedule mail to datesend email"""
    if not isinstance(id_, int):
        raise IdIsNotTypeIntError
    if method not in ["DELETE", "INSERT", "UPDATE"]:
        raise InvalidMethodValueError

    name = f"Send mail {id_}"

    if obj := Schedule.objects.filter(func=func, name=name):
        obj.delete()

    if method in ["INSERT", "UPDATE"]:
        Schedule.objects.create(func=func, kwargs={'id_': id_},
                                name=name, schedule_type=Schedule.ONCE,
                                next_run=date)

# For test mails
# def schedule_cron_test_mail_group_1(name="Test daily cron mail (group 1)",
#                                     func=f"{__package__}.models.email_message.EmailMessage.send_mail_to_all_members"):
#     Schedule.objects.create(func=func, kwargs={'id_': id_},
#                             name=name, schedule_type=Schedule.ONCE,
#                             next_run=date)