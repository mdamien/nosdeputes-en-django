from .base_settings import *

INSTALLED_APPS = ['core'] + INSTALLED_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
    	'NAME': 'cpc',
		'USER': 'cpc',
		'PASSWORD': 'password',
    }
}