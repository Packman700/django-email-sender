""" File store all schedule create functions """

from django_q.tasks import Schedule
from django_newsletter.exceptions import (IdIsNotTypeIntError,
                                          InvalidMethodValueError)


def validate_mail_schedule_input(id_, method):
    if not isinstance(id_, int):
        raise IdIsNotTypeIntError
    if method not in ["DELETE", "SAVE"]:
        raise InvalidMethodValueError


def schedule_delete_not_confirmed_members(name="Delete not confirmed members",
                                          func=f'{__package__}.models.member.Member.delete_not_confirm_members'):
    """Schedule deletion not confirmed members"""
    if obj := Schedule.objects.filter(func=func, name=name):
        obj.delete()

    Schedule.objects.create(func=func, name=name, schedule_type=Schedule.DAILY)


def schedule_mail_message_to_date(mail, method,
                                  func=f"{__package__}.models.email_message.EmailMessageToDate.send_mail_to_all_members"):
    """Schedule mail send to specific date"""
    validate_mail_schedule_input(mail.id, method)
    name = f"Send (date) mail {mail.id}"

    if obj := Schedule.objects.filter(func=func, name=name):
        obj.delete()

    if method == "SAVE":
        Schedule.objects.create(func=func, kwargs={'id_': mail.id},
                                name=name, schedule_type=Schedule.ONCE,
                                next_run=mail.send_time)


def schedule_mail_message_cron(mail, method,
                               func=f"{__package__}.models.email_message.EmailMessageCron.send_mail_to_all_members"):
    """Schedule mail send according to cron expression"""
    validate_mail_schedule_input(mail.id, method)
    name = f"Send (cron) mail {mail.id}"

    if obj := Schedule.objects.filter(func=func, name=name):
        obj.delete()

    if method == "SAVE":
        Schedule.objects.create(func=func, kwargs={'id_': mail.id},
                                name=name, schedule_type="C",
                                cron=mail.cron)


def schedule_mail_message_membership_time(mail, method,
                                          func=f"{__package__}.models.email_message.EmailMessageMembershipTime.send_mail_to_all_members"):
    """Schedule mail send according to time spend from join"""
    validate_mail_schedule_input(mail.id, method)
    name = f"Send (membership time) mail {mail.id}"

    if obj := Schedule.objects.filter(func=func, name=name):
        obj.delete()

    if method == "SAVE":
        Schedule.objects.create(func=func, kwargs={'id_': mail.id},
                                name=name, schedule_type="C",
                                cron="0 6 * * *")  # Run every day in 6 AM
