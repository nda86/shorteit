import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url
import yaml
import logging
import logging.config


load_dotenv(dotenv_path='.env')

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = Path(__file__).resolve().parent


SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = ['*']
BASE_URL = os.environ.get("BASE_URL", "http://localhost:8000")


# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'main',
    'api',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'main.middlewares.SetUserIdMiddleware',
    'main.middlewares.CatchUnhadledException',

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


DATABASES = {'default': dj_database_url.parse(url=os.environ.get("SQL_DATABASE_URI"))}


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


# бэкенд для системы кэширования django
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get("CACHE_REDIS_URL"),
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
STATICFILES_DIRS = []
STATIC_ROOT = os.path.join(BASE_DIR, "static")


# сичтываем и загружаем настройки для логирования
with open(os.path.join(ROOT_DIR, "log_config.yml")) as f:
    logging.config.dictConfig(yaml.safe_load(f.read()))


# насройки drf. Указываем что user без аутентификации будет None. Это что бы drf работал без django.contrib.admin
REST_FRAMEWORK = {
    'UNAUTHENTICATED_USER': None,
}

# настройки для Celery
CELERY_BROKER_URL = os.environ.get("CELERY_REDIS_URL")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_REDIS_URL")
CELERY_BEAT_SCHEDULE = {
    'clear_shorturl_table': {
        'task': 'clear_shorturl',
        'schedule': 60 * 60
    }
}
