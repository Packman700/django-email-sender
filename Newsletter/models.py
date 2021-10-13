import uuid
from datetime import datetime, timedelta

from django.db import models


class Member(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    confirmed = models.BooleanField(default=False)
    username = models.CharField(max_length=50)
    join_datetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.id} {self.email}"

    @classmethod
    def delete_not_confirm_members(cls):
        """Function delete all not confirmed accounts
        after two days email no confirmation
        """
        objects = cls.objects.filter(confirmed=False,
                                     join_datetime__lte=datetime.now() - timedelta(days=2))
        objects.delete()


class EmailMessage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    send_time = models.DateTimeField()
    is_send = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} {self.title}"

    # def send_mail_to_all_members(self):
    #     members_objects = Member.objects.filter(content=True)
    #     members_dic = [
    #         {'email': member.email,
    #          'name': member.name} for
    #         member in
    #         members_objects
    #     ]
    #     print(members_dic)
    #     self.is_send = False


class List(models.Model):
    """ For storing emails in white and black list """
    email_domain = models.CharField(max_length=255)

    class Meta:
        abstract = True

    @classmethod
    def contains(cls, domain):
        """Constrain is finding by simple string.endswith()"""
        objects = cls.objects.all()
        for obj in objects:
            if domain.endswith(obj.email_domain):
                return True
        return False

    def __str__(self):
        return self.email_domain


class WhiteList(List):
    pass


class BlackList(List):
    pass
