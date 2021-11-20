from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from django.contrib import messages

from django_newsletter.form import JoinNewsletterForm
from django_newsletter.models.member import Member


class JoinNewsletter(FormView):
    """This template is main page hold join newsletter logic"""
    template_name = f"{__package__}/views/join_newsletter.html"
    form_class = JoinNewsletterForm
    success_url = reverse_lazy("newsletter:join-newsletter")

    def form_invalid(self, form):
        self.invalid_submits_counter += 1
        return super().form_invalid(form)

    def form_valid(self, form):
        if self.use_recaptcha:
            del self.valid_submits_counter
        del self.invalid_submits_counter
        self.valid_submits_counter += 1

        obj = form.save()
        self.set_message(obj)
        return super().form_valid(form)

    def get_form(self, form_class=None):
        use_recaptcha = self.use_recaptcha
        print(f"{use_recaptcha=}\n{self.valid_submits_counter=}\n{self.invalid_submits_counter=}")
        if use_recaptcha:
            return self.form_class(use_recaptcha=True, **self.get_form_kwargs())
        return self.form_class(**self.get_form_kwargs())

    def set_message(self, obj):
        if obj.confirmed:
            return messages.success(self.request, "Welcome in newsletter <3")
        return messages.info(self.request, f"Almost done. Check <strong>{obj.email}</strong> and confirm join to newsletter")

    # Property
    @property
    def invalid_submits_counter(self):
        return self.request.session.get("InvalidSubmitsCounter", 0)

    @invalid_submits_counter.setter
    def invalid_submits_counter(self, value):
        self.request.session["InvalidSubmitsCounter"] = value

    @invalid_submits_counter.deleter
    def invalid_submits_counter(self):
        del self.request.session["InvalidSubmitsCounter"]

    @property
    def valid_submits_counter(self):
        return self.request.session.get("ValidSubmitsCounter", 0)

    @valid_submits_counter.setter
    def valid_submits_counter(self, value):
        self.request.session["ValidSubmitsCounter"] = value

    @valid_submits_counter.deleter
    def valid_submits_counter(self):
        del self.request.session["ValidSubmitsCounter"]

    @property
    def use_recaptcha(self):
        invalid_submits_counter = self.invalid_submits_counter
        valid_submits_counter = self.valid_submits_counter
        if invalid_submits_counter > 4 or valid_submits_counter > 0:
            return True
        else:
            return False


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
