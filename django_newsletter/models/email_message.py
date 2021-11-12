from django.conf import settings
from django.core.mail import send_mail
from django.db import models

from django_newsletter.mail_factory import default_mail
from django_newsletter.models.member import Member

# from datetime import datetime, timedelta


class EmailMessageAbstract(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.id} {self.title}"

    @classmethod
    def send_mail_to_all_members(cls, id_, members=None):
        """Sending mail to all members"""
        if members is None:
            members_objects = Member.objects.filter(confirmed=True)
        else:
            members_objects = members

        mail = cls.objects.filter(id=id_).first()

        sender_email = settings.EMAIL_HOST_USER
        members_mails = [member.email for member in members_objects]
        email_content = default_mail(mail.content)

        send_mail(mail.title, "", sender_email, members_mails, html_message=email_content)


### DATE EMAIL ###
class EmailMessageToDate(EmailMessageAbstract):
    send_time = models.DateTimeField()
    is_send = models.BooleanField(default=False)

    @classmethod
    def send_mail_to_all_members(cls, id_, members=None):
        """Sending mail to all members"""
        super().send_mail_to_all_members(id_)

        mail = cls.objects.filter(id=id_)
        mail.update(is_send=True)


### CRON EMAIL ###
class EmailMessageCron(EmailMessageAbstract):
    # TODO Add cron validator
    cron = models.CharField(max_length=30)


# class EmailMessageMembershipTime(EmailMessageAbstract):
#     """Send mail according to time left from join"""
#     class Meta:
#         class_name = "EmailMessageMembershipTime"
#         schedule_function_name = "schedule_mail_message_membership_time"
#
#     days_from_join = models.IntegerField(blank=True, default=0, help_text="Number of days spend from join to send this message")
#     date = models.DateField(auto_now_add=True, blank=True)
#
#     @classmethod
#     def send_mail_to_all_members(cls, id_, members=None, **kwargs):
#         """Sending mail to all members"""
#         mail = cls.objects.get(id=id_)
#         mail.date
#         now = datetime.now()
#         days = datetime(day=kwargs['days'])
#
#         members = Member
#
#         super(EmailMessageToDate).send_mail_to_all_members(id_, members)
