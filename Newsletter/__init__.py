"""code bellow makes that ready() run only once on start"""
import os

if os.environ.get('RUN_MAIN', None) != 'true':
    default_app_config = 'mydjangoapp.apps.MydjangoappConfig'