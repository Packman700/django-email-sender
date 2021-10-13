"""The file holds functions that
   are used to generate e-mails"""

from django.template.loader import render_to_string
from .models import Member


def welcome_mail(uuid):
    object_ = Member.objects.get(uuid=uuid)
    context = {
        'uuid': uuid,
        'object': object_,
    }
    return render_to_string("mails/welcome.html", context).replace('\n', '')
