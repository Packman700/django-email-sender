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

    def form_valid(self, form):
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
