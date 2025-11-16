"""
Django settings for LibraryProject project.
Sécurisation des paramètres selon les meilleures pratiques.
"""

import os
from pathlib import Path

# Chemin de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# PARAMÈTRES DE SÉCURITÉ
# -----------------------

# Ne jamais laisser DEBUG = True en production
DEBUG = False

# Clé secrète : à générer et garder confidentielle
# Dans un vrai projet, charger depuis une variable d'environnement
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'remplacez_par_votre_cle_secrete')

# Hôtes autorisés
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'votre_domaine.com']

# -----------------------
# APPLICATIONS INSTALLÉES
# -----------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',  # Votre application
    'csp',        # Middleware Content Security Policy
]

# -----------------------
# MIDDLEWARE
# -----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Protection CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMid
