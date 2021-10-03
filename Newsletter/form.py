from django import forms
from django.forms import ModelForm
from .models import Member
from django.core.mail import send_mail
from os import environ
from django.conf import settings
from .mail_factory import JoinNewsletterWelcomeMail
from django.urls import reverse, resolve


class JoinNewsletterForm(ModelForm):
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
        sender_email = environ.get('EMAIL_USER')
        recipient_email = self.cleaned_data['email']
        title = settings.WELCOME_MAIL_TITLE

        url = reverse('newsletter:welcome-mail', kwargs={'uuid': uuid})
        # ZRÓB Z TEGO STRING
        print(resolve(url))

        # template_body = JoinNewsletterWelcomeMail.as_view(need_confirm=self.NEED_CONFIRM, uuid=uuid)
        # print(template_body())
        # send_mail(title,
        #           template_body,
        #           sender_email,
        #           [recipient_email],
        #           fail_silently=False  # FOR  TEST
        #           )
        #
        # if self.NEED_CONFIRM:
        #     SEND MAIL
            # pass

    def clean_confirmed(self):
        self.confirmed = not self.NEED_CONFIRM
        return self.confirmed

    def clean_email(self):
        #  WALIDATIONS HERE
        email = self.cleaned_data['email']
        return email
