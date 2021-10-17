# Setup
1. pip install -r requirements.txt 

2. Add these settings to project settings
``` Py
INSTALLED_APPS = [
    ...,
    'django_newsletter',  # Main app
    'django_q'  # Async tasks
]

MIDDLEWARE = [
    ...,
    'admin_reorder.middleware.ModelAdminReorder'  # Reorder admin view
]

# DJANGO_Q CONFIG
# doc https://django-q.readthedocs.io/en/latest/configure.html
# Example config for djangoORM
Q_CLUSTER = {
    'name': 'DjangORM',
    'workers': 4,
    'timeout': 90,
    'retry': 120,
    'queue_limit': 50,
    'bulk': 10,
    'orm': 'default'
}
```
3. *If you use ADMIN_REORDER add this line of code
``` Py
ADMIN_REORDER = (
    ...,
    "django_newsletter",
) 
```
4. Add app to urls
``` Py
   urlpatterns = [
      ...,
      path('mail/', include('django_newsletter.urls'))
   ]
```
5. Config smtp server
   - If you use google smtp you can use this config:
     ``` Py
       settings.EMAIL_HOST_USER = environ.get('EMAIL_USER')
       settings.EMAIL_HOST_PASSWORD = environ.get('EMAIL_PASSWORD')  # If you want you can use string
       settings.EMAIL_HOST = "smtp.gmail.com"
       settings.EMAIL_PORT = 587
       settings.EMAIL_USE_TLS = True
     ```
   - **ATTENTION** You need on ```Access to less secure applications``` in your Gmail account
6. Adjust app preferences to your needs (look bellow)
5. manage.py makemigrations
6. manage.py migrate
7. manage.py qcluster 
8. manage.py runserver

Now you can add new mails to newsletter using admin view

# Overwrite template
If you want you can overwrite default templates. By create reconstruct file structure
showed bellow.

Templates to overwrite (to get basic template structure check package repo)
```
your_project
     |-- your_project/
     |-- myapp/
     |-- templates/
          |-- django_newsletter/
              |-- mails/
                  |-- default_mail.html
                  |-- root.html
                  |-- welcome.html
              |-- views/
                  |-- join_newsletter.html
                  |-- join_newsletter_confirm.html
                  |-- join_newsletter_success.html
```

# Preferences default values
``` py
WELCOME_MAIL_TITLE = "Welcome friend - Confirm Your Account"

LOCAL_HOST_NAME = "127.0.0.1:8000"   

NEED_CONFIRM_JOIN_TO_NEWSLETTER = True
AFTER_HOW_MANY_DAYS_DELETE_USER = 1  # Delete only not confirmed users

ENABLE_WHITE_LIST = False  # Accept only mails with suffix in white list table 
ENABLE_BACK_LIST = False  # Accept only mails with suffix with is not in black list table 
```

# Info
Module support Site domain (but I don't test this yet) :)