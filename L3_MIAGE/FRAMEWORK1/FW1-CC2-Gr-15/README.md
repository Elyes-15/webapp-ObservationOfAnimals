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