"""code bellow makes that ready() run only once on start"""
import os
import sys

if 'runserver' in sys.argv and os.environ.get('RUN_MAIN', None) != 'true':
    default_app_config = 'mydjangoapp.apps.MydjangoappConfig'