from django.views.generic import FormView, TemplateView
from .form import JoinNewsletterForm
from django.urls import reverse, reverse_lazy

class JoinNewsletter(FormView):
    template_name = "join_newsletter.html"
    form_class = JoinNewsletterForm
    success_url = reverse_lazy('newsletter:join-newsletter-success')
    # user_email = None

    # def post(self):
    #     pass

    def form_valid(self, form):
        form.send_confirm_mail()
        # self.user_email = form.cleaned_data['email']
        return super().form_valid(form)

    # def get_success_url(self):
    #     pass

class JoinNewsletterSuccess(TemplateView):
    pass
# Create your views here.
