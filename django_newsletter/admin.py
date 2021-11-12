from django.contrib import admin

from django_newsletter.models.access_lists import BlackList, WhiteList
from django_newsletter.models.email_message import EmailMessageToDate, EmailMessageCron #,EmailMessageMembershipTime

from django_newsletter.models.member import Member

admin.site.register(Member)
admin.site.register(BlackList)
admin.site.register(WhiteList)


class ModelAdminModifiedDelete(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        """ Overwrite default delete method """
        for obj in queryset:
            obj.delete()


class EmailMessageToDateAdmin(ModelAdminModifiedDelete):
    model = EmailMessageToDate


class EmailMessageCronAdmin(ModelAdminModifiedDelete):
    model = EmailMessageCron


# class EmailMessageMembershipTimeAdmin(ModelAdminModifiedDelete):
#     model = EmailMessageMembershipTime


admin.site.register(EmailMessageToDate, EmailMessageToDateAdmin)
admin.site.register(EmailMessageCron, EmailMessageCronAdmin)
# admin.site.register(EmailMessageMembershipTime, EmailMessageMembershipTimeAdmin)
