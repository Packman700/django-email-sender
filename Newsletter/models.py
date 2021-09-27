from django.db import models
from datetime import datetime

class Member(models.Model):
    email = models.EmailField()
    confirmed = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    join_datetime = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.id} {self.email}"

class EmailMessage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    send_time = models.DateTimeField()

    def __str__(self):
        return f"{self.id} {self.title}"

# Create your models here.
