import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-i0#!(z)yqe41+f!)h&&k*hft-g&p%!&zv9p_z(0sxma@8q0+rh'

DEBUG = True

ALLOWED_HOSTS = ['indbank.herokuapp.com','127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}


#token git  = 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