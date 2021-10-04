from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import Member
from .mail_factory import welcome_mail


class JoinNewsletterForm(forms.ModelForm):
    NEED_CONFIRM = True

    confirmed = forms.BooleanField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Member
        fields = [
            'email',
            'name',
            'confirmed'
        ]

    def send_confirm_mail(self, uuid):
        title = settings.WELCOME_MAIL_TITLE
        sender_email = settings.EMAIL_HOST_USER
        recipient_email = self.cleaned_data['email']
        email_content = welcome_mail(uuid)

        send_mail(title, "", sender_email, [recipient_email],
                  # ['domciotv2002@gmail.com'],
                  html_message=email_content,
                  )

    def clean_confirmed(self):
        self.confirmed = not self.NEED_CONFIRM
        return self.confirmed

    def clean_email(self):
        #  WALIDATIONS HERE BAN LIST
        email = self.cleaned_data['email']
        return email
