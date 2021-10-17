"""The file holds functions that
   are used to generate e-mails"""

from django.template.loader import render_to_string


def welcome_mail(uuid, object_):
    context = {
        'uuid': uuid,
        'object': object_,
    }
    return render_to_string(f"{__package__}/mails/welcome.html", context).replace('\n', '')

def default_mail(mail_body):
    return render_to_string(f"{__package__}/mails/default_mail.html", {'mail_body': mail_body})
