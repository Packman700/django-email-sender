from django.contrib import admin

from .models import (Member,
                     EmailMessage,
                     BlackList,
                     WhiteList)

admin.site.register(Member)
admin.site.register(BlackList)
admin.site.register(WhiteList)


class EmailMessageAdmin(admin.ModelAdmin):
    model = EmailMessage

    def delete_queryset(self, request, queryset):
        """ Overwrite default delete method """
        for obj in queryset:
            obj.delete()


admin.site.register(EmailMessage, EmailMessageAdmin)
