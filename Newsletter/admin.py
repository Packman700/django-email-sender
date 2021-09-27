from django.contrib import admin
from .models import Member, EmailMessage


admin.site.register(Member)
admin.site.register(EmailMessage)
# Register your models here.
