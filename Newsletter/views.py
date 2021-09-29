from django.views.generic import FormView, TemplateView
from django.views.generic.base import View
from django.shortcuts import render

from .form import JoinNewsletterForm
from django.urls import reverse, reverse_lazy

class JoinNewsletter(View):
    template_name = "join_newsletter.html"
    success_template_name = "join_newsletter_success.html"
    form_class = JoinNewsletterForm
    context = {}
    success_url = reverse_lazy('newsletter:join-newsletter-success')
    user_email = None
    is_bound = True

    def get(self, request, *args, **kwargs):
        return render(request, self.get_template_names(), self.get_context_data())

    def post(self, request):
        if self.get_context_data()['form'].is_valid(self):
            self.form_valid(self.get_context_data())
        return render(request, self.get_template_names(), self.get_context_data())

    def get_context_data(self, *args, **kwargs):
        self.context['form'] = self.form_class
        self.context['email'] = self.user_email if self.user_email else None

        return self.context

    def get_template_names(self):
        print(self.user_email)
        if self.user_email:
            return self.success_template_name
        return self.template_name

    def form_valid(self, form):
        form.send_confirm_mail()
        self.user_email = form.cleaned_data['email']
        return super().form_valid(form)


class JoinNewsletterSuccess(TemplateView):
    user_email = None
    pass
# Create your views here.
