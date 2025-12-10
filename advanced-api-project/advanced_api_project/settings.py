"""
Django settings for advanced_api_project project.
"""

from pathlib import Path

# 🔹 Chemin de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔹 Clé secrète (à changer pour prod)
SECRET_KEY = 'django-insecure-your-secret-key'

# 🔹 Mode debug
DEBUG = True

ALLOWED_HOSTS = []

# 🔹 Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',  # Django REST Framework

    'api',  # Ton application API
]

# 🔹 Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🔹 URLs racine du projet
ROOT_URLCONF = 'advanced_api_project.urls'

# 🔹 Templates
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

# 🔹 WSGI
WSGI_APPLICATION = 'advanced_api_project.wsgi.application'

# 🔹 Base de données (SQLite pour ALX)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔹 Mot de passe / validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🔹 Langue et fuseau horaire
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 🔹 Fichiers statiques
STATIC_URL = '/static/'

# 🔹 Valeur par défaut pour les clés auto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔹 Django REST Framework settings (optionnel)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
