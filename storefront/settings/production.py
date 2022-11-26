import os
from .common import *

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['mybuy-prod.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DBNAME'],
        'HOST': os.environ['DBHOST'],
        'USER': os.environ['DBUSER'],
        'PASSWORD': os.environ['DBPASS']
    }
}
