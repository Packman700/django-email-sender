# Setup
1. pip install -r requirements.txt 

2. Add these settings to project settings
```
INSTALLED_APPS = [
    ...
    'Newsletter',  # Main app
    'django.contrib.sites',  # Get domain name
    'admin_reorder',  # Reorganise admin structure
    'django_q',  # For schedule model tasks
]

MIDDLEWARE = [
    ...
    'admin_reorder.middleware.ModelAdminReorder',  # reorganise admin structure
]

# REORGANISE ADMIN PAGE
ADMIN_REORDER = (
    # Default django models
    {'app': 'auth', 'label': 'Authorisation'},
    # "your_app_1",
    # "your_app_2",
)

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

3. Config Newsletter app settings
   - Set ```login``` and ```password``` for smtp client
   - Config smtp server
   - If you want you can set change preferences and templates
4. manage.py makemigrations
5. manage.py migrate
6. manage.py qcluster
7. manage.py runserver

You can add new mails to newsletter using admin view

If you want you can edit templates 

