from django import forms
from .exceptions import WhiteListValidationError, BlackListValidationError
from django.core.mail import send_mail
from django.conf import settings
from .models import Member, WhiteList, BlackList
from .mail_factory import welcome_mail


class JoinNewsletterForm(forms.ModelForm):
    NEED_CONFIRM = settings.NEED_CONFIRM_JOIN_TO_NEWSLETTER

    confirmed = forms.BooleanField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Member
        fields = [
            'email',
            'username',
            'confirmed'
        ]

    def send_confirm_mail(self, uuid):
        title = settings.WELCOME_MAIL_TITLE
        sender_email = settings.EMAIL_HOST_USER
        recipient_email = self.cleaned_data['email']

        object_ = Member.objects.get(uuid=uuid)
        email_content = welcome_mail(uuid, object_)

        send_mail(title, "", sender_email, [recipient_email], html_message=email_content)

    def clean_confirmed(self):
        self.confirmed = not self.NEED_CONFIRM
        return self.confirmed

    def clean_email(self):
        email = self.cleaned_data['email']
        if settings.ENABLE_WHITE_LIST and not WhiteList.contains(email):
            valid_domains = WhiteList.objects.first().email_domain
            raise WhiteListValidationError(
                "Your email isn't in whitelist you can try %(valid_domain)s",
                params={'valid_domain': valid_domains},
                code='white list error'
            )

        if settings.ENABLE_BACK_LIST and BlackList.contains(email):
            raise BlackListValidationError(
                "Your email is in blacklist try something else",
                code='black list error'
            )

        return email
