from .base import *

ALLOWED_HOSTS = ['3.37.35.152']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': '_R,YX1N0:2s$EKiws{I5M~{07h_H3h5M',
        'HOST': 'ls-5b187f239e96a3e36920a7004aa88534b5e5a8bd.c4u3fdj0tyky.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}