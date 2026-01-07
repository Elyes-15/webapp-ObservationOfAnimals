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
    volumes:
      - .:/home/user/workspace
    ports:
      - "8088:8000"
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
    path('', views.about, name='home'),      # page d'accueil
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
 dans admin.py : on tape  admin.site.register(Animal) .

 ## 2.2.5– Ajouter des animaux et créer un fixture

Commandes utilisées :

```bash
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