from django.template.loader import render_to_string

from django.conf import settings
from .models import Member

def welcome_mail(uuid):
    object_ = Member.objects.get(uuid=uuid)
    context = {
        'uuid': uuid,
        'object': object_,
        'mail_body': settings.WELCOME_MAIL_BODY
    }
    return render_to_string("mails/welcome.html", context).replace('\n', '')

