from django_q.tasks import Schedule
from django_newsletter.exceptions import (IdIsNotTypeIntError,
                                          InvalidMethodValueError)


ROOT_PACKAGE = __package__.split(".")[0]

### HELPERS ###
def validate_mail_schedule_input(id_, method):
    if not isinstance(id_, int):
        raise IdIsNotTypeIntError
    if method not in ["DELETE", "SAVE"]:
        raise InvalidMethodValueError


### SCHEDULE MAILS ###
def schedule_mail_message_to_date(mail, method,
                                  func=f"{ROOT_PACKAGE}.models.email_message.EmailMessageToDate.send_mail_to_all_members"):
    """Schedule mail send to specific date"""
    validate_mail_schedule_input(mail.id, method)
    name = f"Send (date) mail {mail.id}"

    if obj := Schedule.objects.filter(func=func, name=name):
        obj.delete()

    if method == "SAVE":
        Schedule.objects.create(func=func, kwargs={'id_': mail.id},
                                name=name, schedule_type="O",
                                next_run=mail.send_time)


def schedule_mail_message_cron(mail, method,
                               func=f"{ROOT_PACKAGE}.models.email_message.EmailMessageCron.send_mail_to_all_members"):
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
                                          func=f"{ROOT_PACKAGE}.models.email_message.EmailMessageMembershipTime.send_mail_to_all_members"):
    """Schedule mail send according to time spend from join"""
    validate_mail_schedule_input(mail.id, method)
    name = f"Send (membership time) mail {mail.id}"

    if obj := Schedule.objects.filter(func=func, name=name):
        obj.delete()

    if method == "SAVE":
        Schedule.objects.create(func=func, kwargs={'id_': mail.id},
                                name=name, schedule_type="C",
                                cron="0 6 * * *")  # Run every day in 6 AM
