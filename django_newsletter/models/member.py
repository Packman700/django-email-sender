import uuid
from datetime import datetime, timedelta

from django.conf import settings
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
        countdown_days = settings.AFTER_HOW_MANY_DAYS_DELETE_USER
        objects = cls.objects.filter(confirmed=False,
                                     join_datetime__lte=datetime.now() - timedelta(days=countdown_days))
        objects.delete()
