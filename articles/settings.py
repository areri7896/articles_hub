"""
Django settings for articles project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
import environ
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
environ.Env.read_env()  # This reads the .env file

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', 'https://vj6-meticulous-rumford.circumeo-apps.net']

CSRF_TRUSTED_ORIGINS = ['https://vj6-meticulous-rumford.circumeo-apps.net']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # myapps
    'main.apps.MainConfig',
    # 'payment.apps.PaymentConfig',
    'django_daraja',
    # 'accounts',
    'rest_framework',

    'crispy_forms',
    'crispy_bootstrap5',

    'django_bootstrap5',


    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'articles.urls'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


WSGI_APPLICATION = 'articles.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# cat myproject/settings.py


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.environ["POSTGRES_DB"],
#         "USER": os.environ["POSTGRES_USER"],
#         "PASSWORD": os.environ["POSTGRES_PASSWORD"],
#         "HOST": os.environ["POSTGRES_HOST"],
#         "PORT": os.environ["POSTGRES_PORT"],
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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



# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'APP': {
#             'client_id': '123',
#             'secret': '456',
#             'key': ''
#         }
#     }
# }

SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.testing.StaticLiveServerTestCase',
]


STATIC_URL = 'static/'
# The directory where static files will be collected in production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), 
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ACCOUNT_SIGNUP_FORM_CLASS = 'main.forms.CustomSignupForm'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
DEFAULT_FROM_EMAIL = 'admin@lasoi.com'


LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'home'

# MPESA_ENVIRONMENT = os.getenv('MPESA_ENVIRONMENT')
# MPESA_CONSUMER_KEY = os.getenv('MPESA_CONSUMER_KEY')
# MPESA_CONSUMER_SECRET = os.getenv('MPESA_CONSUMER_SECRET')
# MPESA_SHORTCODE = os.getenv('MPESA_SHORTCODE')
# MPESA_PASSKEY = os.getenv('MPESA_PASSKEY')
# MPESA_EXPRESS_SHORTCODE = os.getenv('MPESA_EXPRESS_SHORTCODE')
# MPESA_SHORTCODE_TYPE = os.getenv('MPESA_SHORTCODE_TYPE')
# MPESA_INITIATOR_USERNAME = os.getenv('MPESA_INITIATOR_USERNAME')

# MPESA_INITIATOR_SECURITY_CREDENTIAL = os.getenv('MPESA_INITIATOR_SECURITY_CREDENTIAL')

MPESA_ENVIRONMENT = 'sandbox'
MPESA_CONSUMER_KEY = 'IkiJuKBDN8GbGRA4n4XK1IiJcUEBfrS45ZRMfMzkbMC4f8xY'
MPESA_CONSUMER_SECRET = 'nUK5P7h1qV97vuQZ6yNtbamtkb4i9mvkGcGfiWvcl8EVqWIJIjGLMscKjgVDHhvv'
MPESA_SHORTCODE = '174379'
MPESA_PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
MPESA_EXPRESS_SHORTCODE = '174379'
MPESA_SHORTCODE_TYPE = 'paybill'
MPESA_INITIATOR_USERNAME = 'request.user'

MPESA_INITIATOR_SECURITY_CREDENTIAL = 'Safaricom999!*!'