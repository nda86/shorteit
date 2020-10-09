import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url
import yaml
import logging
import logging.config


load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = Path(__file__).resolve().parent


SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = False
ALLOWED_HOSTS = ['*']
BASE_URL = "http://127.0.0.1:8090"


# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'apps.main',
    'apps.api',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',



    'apps.main.middlewares.SetUserIdMiddleware',
    'apps.main.middlewares.CatchUnhadledException',

]
ROOT_URLCONF = 'shorteit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shorteit.wsgi.application'


DATABASES = {'default': dj_database_url.parse(url=os.environ["SQL_DATABASE_URI"])}


# Password validation
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


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get("CACHE_REDIS_URI"),
        'KEY_PREFIX': 'shortit_cache'
    }
}

# Internationalization
LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

with open(os.path.join(ROOT_DIR, "log_config.yml")) as f:
    logging.config.dictConfig(yaml.safe_load(f.read()))


REST_FRAMEWORK = {
    'UNAUTHENTICATED_USER': None,
}