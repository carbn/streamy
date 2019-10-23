from .settings import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = ast.literal_eval(os.environ.get('DEBUG', 'False'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}
