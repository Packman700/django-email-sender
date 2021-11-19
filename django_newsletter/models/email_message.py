from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone

from django_newsletter.mail_factory import default_mail
from django_newsletter.models.member import Member


class EmailMessageAbstract(models.Model):
    class Meta:
        abstract = True

    database_title = models.CharField(max_length=100, blank=True,
                                      help_text="This title is mail representation in database "
                                                "leave blank if database title should be taken from title")
    title = models.CharField(max_length=100, help_text="This is mail title")
    content = models.TextField()
    send_to_confirmed = models.BooleanField(default=True)
    send_to_not_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} {self.database_title}"

    @classmethod
    def send_mail_to_all_members(cls, id_, members=None):
        """Sending mail to all members"""
        mail = cls.objects.filter(id=id_).first()

        if members is None:
            members = Member.objects.all()

        # Send mail to confirmed or not confirmed users
        if not mail.send_to_confirmed:
            members = members.exclude(confirmed=True)
        if not mail.send_to_not_confirmed:
            members = members.exclude(confirmed=False)
        if not members:
            return

        sender_email = settings.EMAIL_HOST_USER

        for member in members:
            email_content = default_mail(mail.content, member)
            send_mail(mail.title, "", sender_email, [member.email], html_message=email_content)


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


### MEMBERSHIP TIME EMAIL ###
class EmailMessageMembershipTime(EmailMessageAbstract):
    """Send mail according to time left from join"""

    days_from_join = models.IntegerField(blank=True, default=0,
                                         help_text="Number of days spend from join to send this message")

    @classmethod
    def send_mail_to_all_members(cls, id_, members=None):
        """Sending mail to members with """
        mail = cls.objects.get(id=id_)
        time_to_add = timedelta(days=mail.days_from_join)
        today = timezone.now().date()
        expected_account_create_date = today - time_to_add

        members = Member.objects.filter(join_datetime__year=expected_account_create_date.year,
                                        join_datetime__month=expected_account_create_date.month,
                                        join_datetime__day=expected_account_create_date.day)

        if members:
            super().send_mail_to_all_members(id_, members)
