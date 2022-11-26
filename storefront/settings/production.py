import os
from .common import *

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['djangowebapi.azurewebsites.net']
print('inside production')
print(os.environ['DBHOST'] + '.postgres.database.azure.com')
print('djangowebapi-server.postgres.database.azure.com')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DBNAME'],
        'HOST': os.environ['DBHOST'] + '.postgres.database.azure.com',
        'USER': os.environ['DBUSER'],
        'PASSWORD': os.environ['DBPASS']
    }
}
