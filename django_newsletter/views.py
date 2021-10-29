from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import FormView, DetailView

from .form import JoinNewsletterForm
from .models.member import Member


# TODO ADD BOOTSTRAP STYLE TO VIEWS
class JoinNewsletter(FormView):
    template_name = f"{__package__}/views/join_newsletter.html"
    form_class = JoinNewsletterForm
    form_id = None

    def form_valid(self, form):
        obj = form.save()
        self.form_id = obj.pk
        uuid = obj.uuid
        form.send_confirm_mail(uuid=uuid)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("newsletter:join-newsletter-success",
                       kwargs={"id": self.form_id})


class JoinNewsletterSuccess(DetailView):
    template_name = f"{__package__}/views/join_newsletter_success.html"
    model = Member

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)


class JoinNewsletterConfirm(DetailView):
    template_name = f"{__package__}/views/join_newsletter_confirm.html"
    model = Member

    def get_object(self, queryset=None):
        uuid = self.kwargs.get("uuid")
        obj = get_object_or_404(self.model, uuid=uuid)
        obj.confirmed = True
        obj.save()
        return obj
