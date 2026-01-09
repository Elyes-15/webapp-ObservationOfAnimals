# FW1-CC2 – Projet Django Observations Animales

## Membres du groupe

    Kamilia Hacini - kamilia.hacini@etu.univ-orleans.fr
    Sarah Chibane - sarah.chibane@etu.univ-orleans.fr
    Elyes Fetmouche- elyes.fetmouche@etu.univ-orleans.fr
    Rayane Touak- rayane.touak@etu.univ-orleans.fr

# 1. Création du projet Django

1. Création du projet Django :
   python manage.py startapp observo
   INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',
   'observo',
   ]

## 1.2. Migration initiales

python manage.py migrate

## 1.3. Configuration Docker

services:
base:
build:
context: .
dockerfile: Dockerfile
args:
USERNAME: elyes
USERID: 1000
container_name: fw1-cc1
command: /bin/bash
tty: true
stdin_open: true
volumes: - .:/home/user/workspace
ports: - "8088:8000"
environment:
PS1: "[ $$(whoami) | \\w ] "

## 1.4. Lancement du serveur Django depuis le conteneur

python manage.py runserver 0.0.0.0:8000

## 2. Vue et template About:

vue:
from django.shortcuts import render
def about(request):
return render(request, 'observo/about.html')

## url:

CC2/urls.py:
from django.contrib import admin
from django.urls import path
from observo import views

urlpatterns = [
path('admin/', admin.site.urls),
path('', views.about, name='home'), # page d'accueil
path('about/', views.about, name='about'),
]

## TEST :

http://127.0.0.1:8088/about/

# 3.Adminsitration Django:

## 3.1.Création d'un superUtil:

python manage.py createsuperuser

## 3.2:Remplissage du formulaire pour le superUtil:

Nom d’utilisateur:elyes

Email:elyes.fetmouche@etu.univ-orleans.fr

Mot de passe:223160638JE

## 3.3:On lance le serveur et on se connecte:

http://127.0.0.1:8088/admin/

## 2.2.4:Gestion des animaux:

Créer un modèle Animal.
pour rendre le modèle disponible dans l’administration Django :
dans admin.py : on tape admin.site.register(Animal) .

## 2.2.5– Ajouter des animaux et créer un fixture

Commandes utilisées :

````bash
# Créer le dossier fixtures
mkdir -p observo/fixtures

# Créer le fichier animals.json avec les données fournies

# Charger les données dans la base SQLite
python manage.py loaddata animals

## 2.2.6– Vue et template pour les détails d'un animal

# Créer la vue animal_detail dans observo/views.py
# Créer le template observo/templates/observo/animal_detail.html
# Ajouter l'URL dans observo/urls.py et inclure dans cc2/urls.py


## 2.2.7 – Liste tabulaire des animaux


# Créer la vue animal_list dans observo/views.py
# Créer le template observo/templates/observo/animal_list.html
# Ajouter l'URL dans observo/urls.py

## 2.2.8 – Ajouter un nouvel animal via formulaire

# Créer le formulaire AnimalForm dans observo/forms.py
# Créer la vue new_animal dans observo/views.py
# Créer le template observo/templates/observo/new_animal.html
# Ajouter l'URL /new_animal dans observo/urls.py

## Question 9 – Supprimer un animal

Commandes et étapes utilisées :

```bash
# Créer la vue delete_animal dans observo/views.py
# Créer le template observo/templates/observo/delete_animal.html
# Ajouter l'URL /delete_animal/n dans observo/urls.py
# Ajouter un lien de suppression dans le tableau de la liste des animaux

## Question 10 – Modifier un animal

Commandes et étapes utilisées :

```bash
# Création de la vue change_animal
# Réutilisation du formulaire AnimalForm avec instance
# Création du template change_animal.html
# Ajout de l'URL /change_animal/n
# Ajout d'un lien de modification dans la liste des animaux

#  18.BARRE DE NAVIG:
1. Création de `base.html` dans `observo/templates/observo/` :
   - Contient le **HTML de base**, l'en-tête `<head>` et le lien vers **Bootstrap 5.3**.
   - Contient une **navbar** avec les menus :
     - À propos
     - Animaux (Liste, Ajouter)
     - Observations (Liste, Ajouter)
   - Toutes les autres pages héritent de `base.html` avec `{% extends 'observo/base.html' %}`.

2. Mise à jour des templates existants pour hériter de `base.html` :
   - `about.html`
   - `animal_list.html`
   - `animal_detail.html`
   - `new_animal.html`
   - `change_animal.html`
   - `delete_animal.html`
   - `liste_observations.html`
   - `detail_observation.html`
   - `new_observ.html`
   - `change_observ.html`
   - `delete_observ.html`

3. Utilisation de **Bootstrap** pour les formulaires et tableaux :
   - Formulaires dans des `card` avec `mt-3` pour espacement.
   - Boutons stylés : `btn btn-success`, `btn btn-secondary`, `btn btn-danger`.
   - Tables avec classes Bootstrap si besoin (`table table-striped` ou `table table-bordered`).

## 19. Authentification et accès restreint

### 19.1 Mise en place de l’authentification Django
L’authentification repose sur le système natif de Django via `django.contrib.auth`.

Les applications suivantes sont utilisées :
- django.contrib.auth
- django.contrib.sessions
- django.contrib.messages

Des vues de connexion, déconnexion et inscription ont été mises en place.

---

### 19.2 Inscription des utilisateurs
Un formulaire d’inscription basé sur `UserCreationForm` a été créé afin de permettre aux utilisateurs de créer un compte.

Fichiers modifiés :
- `observo/forms.py` : création du formulaire `RegisterForm`
- `observo/views.py` : création de la vue `register`
- `observo/templates/observo/register.html` : template d’inscription

L’URL `/register/` permet à un utilisateur de s’inscrire.

---

### 19.3 Connexion et déconnexion
Les fonctionnalités de connexion et de déconnexion utilisent les vues intégrées de Django :
- `LoginView`
- `LogoutView`

URLs associées :
- `/login/`
- `/logout/`

Après connexion, l’utilisateur est redirigé vers la page d’accueil.

---

### 19.4 Protection des vues
Les vues sensibles sont protégées à l’aide du décorateur `@login_required`, notamment :
- liste des observations
- détail d’une observation
- ajout, modification et suppression d’observations
- accès à la gestion des animaux

Un utilisateur non connecté est automatiquement redirigé vers la page de connexion.

---

## 20. Gestion des rôles : utilisateur et administrateur

### 20.1 Objectif
Mettre en place deux types d’utilisateurs :
- **Utilisateur simple** : accès en lecture seule
- **Administrateur** : accès complet (CRUD)

---

### 20.2 Choix technique
La distinction des rôles repose sur l’attribut `is_staff` du modèle `User` de Django.

Ce choix permet :
- une intégration native avec Django
- une gestion simple et efficace des permissions
- une compatibilité avec l’interface d’administration Django

---

### 20.3 Attribution du rôle lors de l’inscription
Lors de l’inscription, un champ permet de définir si l’utilisateur est administrateur.

Traitement côté serveu
````
