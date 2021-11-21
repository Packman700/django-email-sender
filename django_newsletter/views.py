from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from django.contrib import messages

from django_newsletter.form import JoinNewsletterForm
from django_newsletter.models.member import Member
from django_newsletter.session import RecaptchaLogicSession


class JoinNewsletter(FormView):
    """This template is main page hold join newsletter logic"""
    template_name = f"{__package__}/views/join_newsletter.html"
    form_class = JoinNewsletterForm
    success_url = reverse_lazy("newsletter:join-newsletter")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = None

    def get_form(self, form_class=None):
        # Can't set value in __init__ because there self.request don't exist
        self.session = RecaptchaLogicSession(self.request)
        use_recaptcha = self.session.use_recaptcha
        if use_recaptcha:
            return self.form_class(use_recaptcha=True, **self.get_form_kwargs())
        return self.form_class(**self.get_form_kwargs())

    def form_invalid(self, form):
        self.session.invalid_submits_counter += 1
        return super().form_invalid(form)

    def form_valid(self, form):
        if self.session.use_recaptcha:
            del self.session.valid_submits_counter
        del self.session.invalid_submits_counter
        self.session.valid_submits_counter += 1

        obj = form.save()
        self.set_message(obj)
        return super().form_valid(form)

    def set_message(self, obj):
        if obj.confirmed:
            return messages.success(self.request, "Welcome in newsletter <3")
        return messages.info(self.request, f"Almost done. Check <strong>{obj.email}</strong> and confirm join to newsletter")


def confirm_join_to_newsletter(request, uuid):
    try:
        obj = Member.objects.get(uuid=uuid)
        obj.confirmed = True
        obj.save()
        messages.success(request, "Welcome in newsletter <3")
    except Member.DoesNotExist:
        messages.error(request, "Account not found")

    return redirect(reverse("newsletter:join-newsletter"))


def delete_mail_from_newsletter(request, uuid):
    try:
        obj = Member.objects.get(uuid=uuid)
        obj.delete()
        messages.success(request, "Your account is deleted successfully <br> I hope you will back soon ;D")
    except Member.DoesNotExist:
        messages.error(request, "Account not found")

    return redirect(reverse("newsletter:join-newsletter"))
