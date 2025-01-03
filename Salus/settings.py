"""
Django settings for Salus project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_random_secret_key()

# Set DEBUG to False for production
DEBUG = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'embed_video',
    'django_ckeditor_5',  # Using django-ckeditor-5
    'appSalus',
    'rosetta',
    'parler',
    'admin_honeypot',
    'defender',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'defender.middleware.FailedLoginMiddleware',
]

ROOT_URLCONF = 'Salus.urls'
CKEDITOR_UPLOAD_PATH = "uploads/"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
             BASE_DIR.joinpath('templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Salus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]






DEFENDER_REDIS_URL = 'redis://localhost:6379/0'






# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'sq'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/SalusWeb/WebSalus/appSalus/static/css/'


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from django.utils.translation import gettext_lazy as _

LANGUAGES = (
    ('sq', _('Albanian')),
    ('en', _('English')),
    ('it', _('Italy')),
)
PARLER_LANGUAGES = {
    None : (
        {'code': 'sq',},
        {'code': 'en',},

        {'code': 'it',},
    ),
    'default': {
        'fallbacks': ['sq'],
        'hide_untranslated': False,
    }
}
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

TRANSLATABLE_MODEL_MODULES = ['appSalus.models']

# CKEDITOR_5_CONFIGS
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|', 'bold', 'italic', 'underline', 'strikethrough',
            'link', 'bulletedList', 'numberedList', 'blockQuote', '|',
            'alignment', 'fontColor', 'fontBackgroundColor', 'removeFormat',
            '|', 'insertTable', 'mediaEmbed', 'undo', 'redo'
        ],
        'height': '300px',
        'width': '100%',
        'fontColor': {
            'colors': [
                {
                    'color': 'black',
                    'label': 'Black'
                }
            ],
            'defaultColor': 'black'
        },
        'styles': [
            {
                'element': 'p',
                'styles': {
                    'color': 'black'
                }
            }
        ]
    },
}