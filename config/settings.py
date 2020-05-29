from .base_settings import *

INSTALLED_APPS = ['core'] + INSTALLED_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'config/db.cnf'),
        },
    }
}