from django.contrib import admin
from .models import (Member,
                     EmailMessage,
                     BlackList,
                     WhiteList)

admin.site.register(Member)
admin.site.register(EmailMessage)
admin.site.register(BlackList)
admin.site.register(WhiteList)
