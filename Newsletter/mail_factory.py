from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.conf import settings
from .models import Member

class JoinNewsletterWelcomeMail(DetailView):
    template_name = "mails/welcome.html"
    model = Member

    need_confirm = None
    id = uuid = None

    def get_object(self, queryset=None):
        uuid = self.kwargs.get("uuid")
        return get_object_or_404(self.model, uuid=uuid)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['mail_body'] = settings.WELCOME_MAIL_BODY
        return context

