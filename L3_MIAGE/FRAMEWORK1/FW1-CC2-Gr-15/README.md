# FW1-CC2 – Projet Django Observations Animales

## Membres du groupe

    Kamilia Hacini - kamilia.hacini@etu.univ-orleans.fr
    Sarah Chibane - sarah.chibane@etu.univ-orleans.fr
    Elyes Fetmouche- elyes.fetmouche@etu.univ-orleans.fr
    Rayane Touak- rayane.touak@etu.univ-orleans.fr


## 1. Création du projet Django

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

## 2. Migration initiales
python manage.py migrate

## 3. Configuration Docker
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


## 4. Lancement du serveur Django depuis le conteneur
python manage.py runserver 0.0.0.0:8000





