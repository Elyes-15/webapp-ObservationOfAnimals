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
<<<<<<< HEAD

http://127.0.0.1:8088/admin/

## 2.2.4:Gestion des animaux:

Créer un modèle Animal.
pour rendre le modèle disponible dans l’administration Django :
dans admin.py : on tape admin.site.register(Animal) .

## 2.2.5– Ajouter des animaux et créer un fixture

Commandes utilisées :

````bash
# Créer le dossier fixtures
=======
http://127.0.0.1:8088/admin/ 
## 2.3.1 : Gestion des observations 

  Création du modèle Observation:

Créer un modele `Observation` dans `observo/models.py`.

Le modèle contient :
- date (DateField)
- heure (TimeField)
- latitude (FloatField)
- longitude (FloatField)
- description (TextField)
- animal (ForeignKey vers Animal)

Pour rendre le modele disponible dans l’administration Django :  
dans `admin.py` : on tape 
```python
admin.site.register(Observation)
```

### Générer les migrations
```bash
python manage.py makemigrations
```

### Appliquer les migrations
```bash
python manage.py migrate
```
### Verifications
-Lancer le serveur Django:
```bash
python manage.py runserver 0.0.0.0:8088
```

-Aller dans l’admin :
```bash
http://127.0.0.1:8088/admin/
```
## 2.3.2 : Ajouter des observations et créer un fixture

Créer le fichier `observations.json` dans `observo/fixtures/`.

Le fichier contient plus de 50 observations différentes, chacune avec :
- une date
- une heure
- une latitude
- une longitude
- une description
- un animal associé (clé étrangère)

Commandes utilisées :

```bash
# Créer le dossier fixtures 
>>>>>>> tests
mkdir -p observo/fixtures

# Créer et remplir le fichier observations.json avec au moins 50 observations

# Charger les données dans la base SQLite
python manage.py loaddata observations

 #Verifications
-Lancer le serveur Django:

python manage.py runserver 0.0.0.0:8088
-et taper sur
 http://127.0.0.1:8088/admin/
 
```
## 2.3.3 : Vue et template pour les détails d'une observation

Créer la vue `observ_detail` dans `observo/views.py`.

Créer le template `observo/templates/observo/observ_detail.html`.

Ajouter l’URL dans `observo/urls.py` et inclure dans `cc2/urls.py`.

Exemple d’URL :  
/observs/n où n est l’identifiant de l’observation.

- Commandes / fichiers modifiés :
```bash
Créer la vue observ_detail dans observo/views.py
Créer le template observo/templates/observo/observ_detail.html
Ajouter l'URL /observs/n dans observo/urls.py
Inclure les URLs dans cc2/urls.py
```
## 2.3.4 : Liste tabulaire des observations

Créer la vue `observ_list` dans `observo/views.py`.

Créer le template `observo/templates/observo/observ_list.html`.

L’URL d’accès doit être `/observs`.

La liste affiche :
- le nom commun de l’animal observé
- la date de l’observation
- la localisation (latitude / longitude)
- un lien vers la fiche détaillée de l’observation

 Commandes / fichiers modifiés :
```bash
Créer la vue observ_list dans observo/views.py
Créer le template observo/templates/observo/observ_list.html
Ajouter l'URL /observs dans observo/urls.py
Inclure les URLs dans cc2/urls.py 
```
## 2.3.5 : Ajouter une nouvelle observation via formulaire

Créer le formulaire `ObservationForm` dans `observo/forms.py`.

Créer la vue `new_observ` dans `observo/views.py`.

Créer le template `observo/templates/observo/new_observ.html`.

L’URL d’accès doit être `/new_observ`.

Le formulaire permet d’ajouter :
- la date
- l’heure
- la latitude
- la longitude
- la description
- l’animal observé

Commandes / fichiers modifiés :
```bash
Créer le formulaire ObservationForm dans observo/forms.py
Créer la vue new_observ dans observo/views.py
Créer le template observo/templates/observo/new_observ.html
Ajouter l'URL /new_observ dans observo/urls.py
Inclure les URLs dans cc2/urls.py 
```

## 2.3.6 : Supprimer une observation

Créer la vue `delete_observ` dans `observo/views.py`.

Créer le template `observo/templates/observo/delete_observ.html`.

L’URL d’accès doit être `/delete_observ/n` où n est l’identifiant de l’observation.

Une page de confirmation doit etre affichee avant la suppression.

Ajouter un lien de suppression dans la liste des observations.

Commandes / fichiers modifiés :
```bash
Créer la vue delete_observ dans observo/views.py
Créer le template observo/templates/observo/delete_observ.html
Ajouter l'URL /delete_observ/n dans observo/urls.py
Inclure les URLs dans cc2/urls.py
Ajouter un lien de suppression dans la liste des observations
```

## 2.3.7 : Modifier une observation

Créer la vue `change_observ` dans `observo/views.py`.

Réutiliser le formulaire `ObservationForm` avec `instance` pour preremplir les champs.

Créer le template `observo/templates/observo/change_observ.html`.

L’URL d’accès doit etre `/change_observ/n` ou n est l’identifiant de l’observation.

Ajouter un lien de modification dans la liste des observations.

Commandes / fichiers modifiés :
```bash
Créer la vue change_observ dans observo/views.py
Réutiliser ObservationForm avec instance
Créer le template observo/templates/observo/change_observ.html
Ajouter l'URL /change_observ/n dans observo/urls.py
Inclure les URLs dans cc2/urls.py
Ajouter un lien de modification dans la liste des observations
```
##  18.BARRE DE NAVIG:
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

<<<<<<< HEAD
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
=======
### Tests réalisés

- **Modèles**
  - `Animal` : création d’un animal et vérification de son `nom_commun`.

- **Vues**
  - Page liste des animaux (`animal_list`)
  - Page liste des observations (`liste_observations`) accessible après login
  - Page d’inscription (`register`) existe et renvoie un status 200

### Exécution

Pour lancer les tests, utiliser :

```bash
python manage.py test
>>>>>>> tests
