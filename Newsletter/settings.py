"""
Set all django configuration related with sending e-mails
HOW PREPARE YOUR YOUR GMAIL ACCOUNT
https://youtu.be/UH8oHNDfTyQ?t=171
"""

from django.conf import settings


def set_settings():
    # VALIDATORS
    add_apps()
    add_admin_reorder()
    valid_login_password()
    valid_is_settings_set()

    # PREFERENCES
    DEFAULT_PREFERENCES = {
        "WELCOME_MAIL_TITLE": "Welcome friend - Confirm Your Account",

        "LOCAL_HOST_NAME": "127.0.0.1:8000",

        "NEED_CONFIRM_JOIN_TO_NEWSLETTER": True,
        "AFTER_HOW_MANY_DAYS_DELETE_USER": 1,

        "ENABLE_WHITE_LIST": False,
        "ENABLE_BACK_LIST": False,
    }
    for setting, default_value in DEFAULT_PREFERENCES.items():
        set_default_if_none(setting, default_value)


def set_default_if_none(setting_name, default_value):
    """This allow to simply set all settings"""
    if getattr(settings, setting_name, None) is None:
        setattr(settings, setting_name, default_value)


def valid_login_password():
    """Check if user set username and password for mail"""
    if not settings.EMAIL_HOST_USER:
        raise TypeError('EMAIL_HOST_USER is None')
    if not settings.EMAIL_HOST_PASSWORD:
        raise TypeError('EMAIL_HOST_PASSWORD is None')


def valid_is_settings_set():
    """Simple settings validator"""
    try:
        settings.ADMIN_REORDER
    except AttributeError:
        raise AttributeError("Add ADMIN_REORDER to your settings")

    try:
        settings.Q_CLUSTER
    except AttributeError:
        raise AttributeError("Add Q_CLUSTER to your settings")


def add_apps():
    """Add needed apps to project"""
    REQUIRED_APPLICATIONS = [
        'admin_reorder',  # Reorganise admin structure
        'django_q',  # For schedule model tasks
    ]

    # settings.INSTALLED_APPS.append('django_q')
    for app_name in REQUIRED_APPLICATIONS:
        if app_name not in settings.INSTALLED_APPS:
            settings.INSTALLED_APPS += app_name


def add_admin_reorder():
    ADMIN_REORDER_PACKAGE_SETTINGS = (
        {
            'app': __package__,
            'label': 'newsletter black/white list',
            'models': (f'{__package__}.WhiteList',
                       f'{__package__}.BlackList')
        },
        {
            'app': __package__,
            'label': 'newsletter',
            'models': (f'{__package__}.EmailMessage',
                       f'{__package__}.Member')
        }
    )

    """Create ADMIN_REORDER file"""
    if getattr(settings, 'ADMIN_REORDER', None) is not None:
        if __package__ in settings.ADMIN_REORDER:
            settings.ADMIN_REORDER = tuple(setting for setting in settings.ADMIN_REORDER if setting != __package__)
            settings.ADMIN_REORDER += ADMIN_REORDER_PACKAGE_SETTINGS
        return None

    settings.ADMIN_REORDER = (
        {'app': 'auth', 'label': 'Authorisation'},
    )

    apps = settings.INSTALLED_APPS
    for app_name in apps:
        if app_name == __package__:
            continue
        settings.ADMIN_REORDER = settings.ADMIN_REORDER + (app_name,)

    settings.ADMIN_REORDER += ADMIN_REORDER_PACKAGE_SETTINGS
