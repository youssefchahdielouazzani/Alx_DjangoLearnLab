# advanced_features_and_security/accounts/models.py

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# ------------------------------
# Custom User Manager
# ------------------------------
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth=None, password=None, **extra_fields):
        """
        Crée et retourne un utilisateur standard.
        """
        if not email:
            raise ValueError('L’adresse email doit être renseignée')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth=None, password=None, **extra_fields):
        """
        Crée et retourne un superutilisateur.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le superutilisateur doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Le superu
