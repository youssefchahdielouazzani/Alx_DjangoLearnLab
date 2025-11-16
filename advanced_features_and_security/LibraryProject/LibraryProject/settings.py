# ===============================
# HTTPS & SECURITY SETTINGS
# ===============================

# Redirige toutes les requêtes HTTP vers HTTPS
SECURE_SSL_REDIRECT = True

# Si Django est derrière un proxy (ex: Nginx), indique que HTTPS est utilisé
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000          # 1 an
SECURE_HSTS_INCLUDE_SUBDOMAINS = True   # Applique HSTS à tous les sous-domaines
SECURE_HSTS_PRELOAD = True              # Permet l'inclusion dans les listes de préchargement des navigateurs

# Cookies sécurisés (uniquement envoyés sur HTTPS)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Headers de sécurité supplémentaires
X_FRAME_OPTIONS = 'DENY'                # Protection contre le clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True      # Bloque les attaques de type MIME sniffing
SECURE_BROWSER_XSS_FILTER = True        # Active le filtrage XSS côté navigateur

