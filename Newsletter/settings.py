"""
Set all django configuration related with sending e-mails
HOW PREPARE YOUR YOUR GMAIL ACCOUNT
https://youtu.be/UH8oHNDfTyQ?t=171
"""

from django.conf import settings
from os import environ
from pathlib import Path

login = environ.get('EMAIL_USER')  # If you want you can use string
password = environ.get('EMAIL_PASSWORD')

def set_settings():
    if login is None:
        raise (TypeError, 'EMAIL_USER is None')
    if password is None:
        raise (TypeError, 'EMAIL_PASSWORD is None')

    # SETUP BACKEND
    settings.EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    settings.EMAIL_HOST = "smtp.gmail.com"
    settings.EMAIL_PORT = 507
    settings.EMAIL_USE_TLS = True
    settings.EMAIL_HOST_USER = login
    settings.EMAIL_HOST_PASSWORD = password

    # WELCOME MAIL
    settings.WELCOME_MAIL_TITLE = "Welcome friend - Confirm Your Account"
    settings.WELCOME_MAIL_BODY = Path('Newsletter/local_static/welcome_mail_body.html').read_text()
