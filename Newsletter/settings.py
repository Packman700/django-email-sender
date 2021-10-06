"""
Set all django configuration related with sending e-mails
HOW PREPARE YOUR YOUR GMAIL ACCOUNT
https://youtu.be/UH8oHNDfTyQ?t=171
"""

from django.conf import settings
from os import environ

login = environ.get('EMAIL_USER')  # If you want you can use string
password = environ.get('EMAIL_PASSWORD')

def set_settings():
    valid_login_password()

    # SETUP BACKEND
    settings.EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    # settings.EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    settings.EMAIL_HOST = "smtp.gmail.com"
    settings.EMAIL_PORT = 587
    settings.EMAIL_USE_TLS = True
    settings.EMAIL_HOST_USER = login
    settings.EMAIL_HOST_PASSWORD = password

    settings.WELCOME_MAIL_TITLE = "Welcome friend - Confirm Your Account"

    settings.LOCAL_HOST_NAME = "127.0.0.1:8000"

    settings.NEED_CONFIRM_JOIN_TO_NEWSLETTER = True

    settings.ENABLE_WHITE_LIST = False
    settings.ENABLE_BACK_LIST = False

def valid_login_password():
    if login is None:
        raise (TypeError, 'EMAIL_USER is None')
    if password is None:
        raise (TypeError, 'EMAIL_PASSWORD is None')
