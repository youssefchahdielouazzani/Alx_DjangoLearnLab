# Advanced Features and Security - Django Project

## Description

Ce projet Django illustre la gestion avancée des utilisateurs, des permissions et des groupes pour contrôler l'accès aux différentes parties de l'application.

Le projet inclut :

- Un **Custom User Model** (`CustomUser`) avec des champs supplémentaires :
  - `date_of_birth` : date de naissance
  - `profile_photo` : photo de profil
- Une application **bookshelf** avec un modèle `Book` et des permissions personnalisées :
  - `can_view` : permission pour voir les livres
  - `can_create` : permission pour créer un livre
  - `can_edit` : permission pour éditer un livre
  - `can_delete` : permission pour supprimer un livre
- Gestion des **groupes d'utilisateurs** :
  - `Viewers` : peuvent uniquement voir les livres
  - `Editors` : peuvent créer et éditer des livres
  - `Admins` : toutes les permissions (voir, créer, éditer, supprimer)

---

## Installation

1. **Cloner le dépôt :**

```bash
git clone https://github.com/<votre-utilisateur>/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/advanced_features_and_security
