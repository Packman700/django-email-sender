"""
Set all django configuration related with sending e-mails
HOW PREPARE YOUR YOUR GMAIL ACCOUNT
https://youtu.be/UH8oHNDfTyQ?t=171
"""

from os import environ

from django.conf import settings

login = environ.get('EMAIL_USER')  # If you want you can use string
password = environ.get('EMAIL_PASSWORD')


def set_settings():
    # VALIDATORS
    valid_login_password()
    valid_apps_and_middleware()
    valid_is_settings_set()

    # SETUP BACKEND
    settings.EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    # settings.EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    settings.EMAIL_HOST = "smtp.gmail.com"
    settings.EMAIL_PORT = 587
    settings.EMAIL_USE_TLS = True
    settings.EMAIL_HOST_USER = login
    settings.EMAIL_HOST_PASSWORD = password

    # PREFERENCES
    settings.WELCOME_MAIL_TITLE = "Welcome friend - Confirm Your Account"

    settings.LOCAL_HOST_NAME = "127.0.0.1:8000"

    settings.NEED_CONFIRM_JOIN_TO_NEWSLETTER = True
    settings.AFTER_HOW_MANY_DAYS_DELETE_USER = 1

    settings.ENABLE_WHITE_LIST = False
    settings.ENABLE_BACK_LIST = False

    # REORGANISE ADMIN PAGE
    settings.ADMIN_REORDER += (
        {'app': __package__,
         'label': 'newsletter black/white list',
         'models': (f'{__package__}.WhiteList',
                    f'{__package__}.BlackList')
         },
        {'app': __package__,
         'label': 'newsletter',
         'models': (f'{__package__}.EmailMessage',
                    f'{__package__}.Member')
         },
    )


def valid_login_password():
    if login is None:
        raise TypeError('EMAIL_USER is None')
    if password is None:
        raise TypeError('EMAIL_PASSWORD is None')


def valid_apps_and_middleware():
    REQUIRED_MIDDLEWARE = 'admin_reorder.middleware.ModelAdminReorder'
    REQUIRED_APPLICATIONS = [
        'django.contrib.sites',
        'admin_reorder',
        'django_q'
    ]

    if REQUIRED_MIDDLEWARE not in settings.MIDDLEWARE:
        raise ImportError(f"{REQUIRED_MIDDLEWARE} not found in INSTALLED_APPS")

    for app_name in REQUIRED_APPLICATIONS:
        if app_name not in settings.INSTALLED_APPS:
            raise ImportError(f"{app_name} not found in INSTALLED_APPS")


def valid_is_settings_set():
    try:
        settings.ADMIN_REORDER
    except AttributeError:
        raise AttributeError("Add ADMIN_REORDER to your settings")

    try:
        settings.Q_CLUSTER
    except AttributeError:
        raise AttributeError("Add Q_CLUSTER to your settings")