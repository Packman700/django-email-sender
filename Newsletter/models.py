from django.db import models
from datetime import datetime
import uuid

class Member(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    confirmed = models.BooleanField(default=False)
    username = models.CharField(max_length=50)
    join_datetime = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.id} {self.email}"


class EmailMessage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    send_time = models.DateTimeField()

    def __str__(self):
        return f"{self.id} {self.title}"


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

# manage.py shell
# from Newsletter.models import BlackList
# BlackList.contains("a")