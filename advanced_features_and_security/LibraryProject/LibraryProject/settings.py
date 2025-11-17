"""
Django settings for LibraryProject.
Configurations de sécurité renforcées pour HTTPS et cookies sécurisés.
"""

from pathlib import Path

# ----------------------------
# Chemins de base du projet
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------
# Clé secrète et debug
# ----------------------------
SECRET_KEY = 'votre-secret-key'  # Remplacez par votre clé réelle
DEBUG = False
ALLOWED_HOSTS = ['votre-domaine.com']  # Remplacez par votre domaine

# ----------------------------
# Applications installées
# ----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
]

# ----------------------------
# Middleware
# ----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

# ----------------------------
# Templates
# ----------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# ----------------------------
# Base de données
# ----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------------------
# Validation des mots de passe
# ----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ----------------------------
# Internationalisation
# ----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------------------
# Fichiers statiques
# ----------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ----------------------------
# CONFIGURATIONS DE SECURITE
# ----------------------------

# Redirection HTTP → HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 an
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Cookies sécurisés
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Protection contre le clickjacking
X_FRAME_OPTIONS = 'DENY'

# Protection contre le MIME sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Protection XSS côté navigateur
SECURE_BROWSER_XSS_FILTER = True

# Pour ALX : HTTPS détecté derrière un proxy (comme Nginx)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ----------------------------
# Champs par défaut
# ----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

