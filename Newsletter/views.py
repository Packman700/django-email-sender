from django.shortcuts import get_object_or_404
from django.views.generic import FormView, DetailView
from .form import JoinNewsletterForm
from .models import Member
from django.urls import reverse

class JoinNewsletter(FormView):
    template_name = "join_newsletter.html"
    form_class = JoinNewsletterForm
    form_id = None

    def form_valid(self, form):
        form.send_confirm_mail()
        obj = form.save()
        self.form_id = obj.pk
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("newsletter:join-newsletter-success",
                       kwargs={"id": self.form_id})


class JoinNewsletterSuccess(DetailView):
    template_name = "join_newsletter_success.html"
    model = Member

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(self.model, id=id_)
