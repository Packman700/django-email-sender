# Fields
from django.forms import ModelForm
from .models import Member

class JoinNewsletterForm(ModelForm):
    need_confirm = True
    class Meta:
        model = Member
        fields = [
            'email',
            'name'
        ]

    def send_confirm_mail(self):
        if self.need_confirm:
            # SEND MAIL
            pass

    def clean_email(self):
        email = self.cleaned_data['email']
        return email