import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x*q-zz=9ri@%m*a6lo=%&!h(6ryu3m++rz^9@anbeg)7&tzud-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'core.apps.CoreConfig',
    'shop.apps.ShopConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login_required',
    'storages',
    #'ajax',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'login_required.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'apdev.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'apdev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'apdevdb',
        'USER': 'postgres',
        'PASSWORD': 'Mu3kata!owieC',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'core.User'

# CACHE bazodanowy. https://docs.djangoproject.com/en/2.2/topics/cache/
# Przed użyciem stwórz tabelę w bazie danych za pomocą:
# "python manage.py createcachetable"
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
        'TIMEOUT': 10,
        'OPTIONS': {
            'MAX_ENTRIES': 2000,
            'CULL_FREQUENCY': 2
        }
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'

CACHE_MIDDLEWARE_SECONDS = 1

CACHE_MIDDLEWARE_KEY_PREFIX = ''

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
# Dla sesji opartych na ciastkach:
# "django.contrib.sessions.backends.signed_cookies"
# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Moduł tłumaczeniowy, jak wszystko z MODELTRANSLATION w nazwie
# https://django-modeltranslation.readthedocs.io/en/latest/
# klasy są tak poustawiane, że dodanie lub usunięcie języka z settings.py
# automatycznie powoduje ich dodanie/usunięcie wszędzie indziej.
# TODO: Poprawić langjs.js żeby też był z tym zsynchronizowany.
gettext = lambda s: s
LANGUAGES = (
    # Pierwszy jest zawsze defaultem chyba, że zrobisz override.
    ('pl', gettext('Polish')),
    ('en', gettext('English')),
    ('ru', gettext('Russian')),
)

LANGUAGE_COOKIE_AGE = 31449600  # Około rok ważności
# Ustaw None jeśli chcesz, żeby się zerowały po każdym wyłączeniu przeglądarki.

LANGUAGE_COOKIE_NAME = 'apdev_language'  # Nazwa ciacha językowego

LANGUAGE_COOKIE_PATH = '/'  # Domyślna ścieżka ciastków.

MODELTRANSLATION_DEFAULT_LANGUAGE = 'pl'  # Tu możesz zmienić default language.

MODELTRANSLATION_LANGUAGES = ('pl', 'en', 'ru',)

# W ten sposób zachowają sie języki jak nie znajdzie się jakiegoś w bazie.
MODELTRANSLATION_FALLBACK_LANGUAGES = {'default': ('en', ), 'en': ('pl', 'ru')}

# Tutaj rejestruje się wszystkie trackery translacyjne.
MODELTRANSLATION_TRANSLATION_FILES = (
    'core.translation',
    'shop.translation',
)
# Konfiguracja CDN
# https://github.com/jschneier/django-storages
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' !!

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' !!

AWS_S3_REGION_NAME = 'fra1'

AWS_S3_ENDPOINT_URL = 'https://apdev.fra1.digitaloceanspaces.com'

# Ustal aktualny access_key w .local_settings
AWS_ACCESS_KEY_ID = 'UY25DNGAOVVGCA2UUK2L'

# Ustal aktualny secret_key w .local_settings
AWS_SECRET_ACCESS_KEY = 'TtICSTYds/ipCuhUfmxZ2cpiV2sp+N+xR6Cp95dN1fw'

AWS_STORAGE_BUCKET_NAME = 'apdev'

AWS_DEFAULT_ACL = None

# AWS_S3_CUSTOM_DOMAIN = 'https://apdev.fra1.cdn.digitaloceanspaces.com'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'apdev/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/'  # Przekierowanie usera po zalogowaniu

LOGOUT_REDIRECT_URL = '/'  # Przekierowanie po wylogowaniu.

# Poniżej dane do ustawień Middleware blokującego strony przed niezalogowanymi.
LOGIN_URL = '/'


# https://github.com/CleitonDeLima/django-login-required-middleware
LOGIN_REQUIRED_IGNORE_PATHS = [
     r'^$',
     r'^static/.*$',
     r'^media/.*$',
     r'^admin/.*$',
]


# Mailing Django. Do podmianki w local_settings.py
# https://www.tutorialspoint.com/django/django_sending_emails.htm
# https://docs.djangoproject.com/en/2.2/topics/email/
EMAIL_HOST = 'localhost'

EMAIL_HOST_USER = ''

EMAIL_HOST_PASSWORD = ''

EMAIL_PORT = 25

EMAIL_USE_SSL = False

EMAIL_SSL_CERTFILE = None

# FILE_UPLOAD_HANDLERS = []

# Ściągnij ustawienia lokalne gdybyśmy chcieli udostępnić kod i wejść na OpenSource
# na serwerze obok "settings" robisz plik .local_settings i ustalasz od nowa:
# SECRET_KEY, DEBUG = False, DATABASES, oraz CACHES jeśli używasz Memccache.
# edit: oraz inne o których było wspomniane wcześniej.
try:
    from .local_settings import *
except ImportError:
    pass
