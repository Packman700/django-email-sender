from django.contrib import admin

from django_newsletter.models.access_lists import BlackList, WhiteList
from django_newsletter.models.email_message import EmailMessageToDate, EmailMessageCron
from django_newsletter.models.member import Member

admin.site.register(Member)
admin.site.register(BlackList)
admin.site.register(WhiteList)


class EmailMessageToDateAdmin(admin.ModelAdmin):
    model = EmailMessageToDate

    def delete_queryset(self, request, queryset):
        """ Overwrite default delete method """
        for obj in queryset:
            obj.delete()


class EmailMessageCronAdmin(admin.ModelAdmin):
    model = EmailMessageCron

    def delete_queryset(self, request, queryset):
        """ Overwrite default delete method """
        for obj in queryset:
            obj.delete()


admin.site.register(EmailMessageToDate, EmailMessageToDateAdmin)
admin.site.register(EmailMessageCron, EmailMessageCronAdmin)
