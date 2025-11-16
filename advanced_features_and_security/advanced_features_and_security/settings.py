import os
from pathlib import Path

# -----------------------------
# BASE DIR
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# -----------------------------
# PARAMÈTRES DE SÉCURITÉ
# -----------------------------
SECRET_KEY = 'django-insecure-change-this-value'

DEBUG = True

ALLOWED_HOSTS = []


# -----------------------------
# APPLICATIONS INSTALLEES
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # --- APP POUR LE CUSTOM USER ---
    'accounts',
]


# -----------------------------
# MIDDLEWARE
# -----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# -----------------------------
# URLS ET CONFIG TEMPLATE
# -----------------------------
ROOT_URLCONF = 'advanced_features_and_security.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'advanced_features_and_security.wsgi.application'


# -----------------------------
# BASE DE DONNÉES
# -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -----------------------------
# VALIDATEURS DE MOTS DE PASSE
# -----------------------------
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


# -----------------------------
# LANGUE ET TIMEZONE
# -----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True


# -----------------------------
# FICHIERS STATIQUES
# -----------------------------
STATIC_URL = 'static/'
STATICFILES_DIRS = []
STATIC_ROOT = BASE_DIR / 'staticfiles'


# -----------------------------
# FICHIERS MEDIA (uploads)
# -----------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# -----------------------------
# CUSTOM USER MODEL
# -----------------------------
# Étape 2 : Indiquer que Django doit utiliser ton modèle CustomUser
AUTH_USER_MODEL = 'accounts.CustomUser'


# -----------------------------
# AUTO FIELD PAR DEFAUT
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
