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

# Question23:
1.1/Création de la carte des observations avec barre de recherche par animal:
vue:
@login_required
def liste_observations(request):
    if est_admin(request.user):
        observations = Observation.objects.all().order_by('-date', '-heure')
    else:
        observations = Observation.objects.filter(utilisateur=request.user).order_by('-date', '-heure')

    # Récupération des animaux pour le filtre
    animaux = Animal.objects.all().order_by('nom_commun')

    return render(request, 'observo/liste_observations.html', {
        'observations': observations,
        'animaux': animaux,
    })

Template:liste_observations:
**inclure la carte: <div id="map" style="height: 500px; margin-bottom: 20px;"></div>
**Ajouter une barre de recherche / filtre :
<select id="animalFilter" class="form-select mb-3">
    <option value="">-- Choisir un animal --</option>
    {% for animal in animaux %}
        <option value="{{ animal.nom_commun }}">{{ animal.nom_commun }}</option>
    {% endfor %}
</select>
** Leaflet:
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
**markers:
<script>
    // Création de la carte centrée sur la France
    var map = L.map('map').setView([46.6, 2.5], 6);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(map);

    // Récupération des observations depuis Django
    var observations = [
        {% for obs in observations %}
        {
            animal: "{{ obs.animal.nom_commun }}",
            lat: {{ obs.latitude }},
            lng: {{ obs.longitude }},
            date: "{{ obs.date }}",
            heure: "{{ obs.heure }}",
            description: "{{ obs.description|default:'Aucune'|escapejs }}"
        },
        {% endfor %}
    ];

    var markers = [];

    observations.forEach(function(obs) {
        var marker = L.marker([obs.lat, obs.lng])
            .addTo(map)
            .bindPopup(
                "<b>" + obs.animal + "</b><br>" +
                "Date: " + obs.date + " " + obs.heure + "<br>" +
                "Description: " + obs.description
            );
        marker.animal = obs.animal;  // pour filtrage
        markers.push(marker);
    });

    // Filtrage par animal
    var select = document.getElementById('animalFilter');
    select.addEventListener('change', function() {
        var selected = this.value;
        markers.forEach(function(marker) {
            if (!selected || marker.animal === selected) {
                marker.addTo(map);
            } else {
                map.removeLayer(marker);
            }
        });
    });
</script>

```

## 23. Extension – Statistiques globales et visualisation des observations

Cette partie de l’extension a pour objectif de fournir une analyse globale des observations enregistrées dans l’application, sous forme de statistiques numériques et de graphes interactifs.

Les statistiques portent sur l’ensemble des observations visibles sur la carte (et non des statistiques personnelles).

---

### 23.1 Objectifs

- Fournir une vue synthétique de l’activité d’observation
- Mettre en valeur les données collectées via des indicateurs clairs
- Visualiser les tendances temporelles et biologiques
- Compléter la carte par une analyse statistique

---

### 23.2 Création de la page Statistiques

Une nouvelle page dédiée a été créée :

- URL : `/stats/`
- Accessible depuis la barre de navigation
- Affiche toutes les statistiques et graphes

Fichiers concernés :

- `observo/views.py`
- `observo/templates/observo/stats.html`
- `observo/urls.py`
- `observo/templates/observo/base.html` (navbar)

---

### 23.3 Statistiques calculées (Django ORM)

Les statistiques sont calculées uniquement à l’aide du **Django ORM**, sans bibliothèque externe côté backend.

Statistiques affichées :

- Nombre total d’observations
- Nombre d’espèces différentes observées
- Animal le plus observé
- Mois avec le plus d’observations

Exemples de requêtes utilisées :

- `Observation.objects.count()`
- `Observation.objects.values('animal').distinct().count()`
- Agrégation avec `Count`
- Regroupement temporel avec `TruncMonth`

---

### 23.4 Graphes et visualisation (Chart.js)

Les données statistiques sont visualisées à l’aide de **Chart.js** côté frontend.

Graphes implémentés :

1. **Histogramme – Observations par mois**

   - Permet d’identifier les périodes les plus actives

2. **Diagramme circulaire (Pie chart) – Répartition par statut IUCN**

   - Visualise l’état de conservation des espèces observées

3. **Histogramme horizontal – Observations par animal**
   - Met en évidence les espèces les plus fréquemment observées

Les graphes sont intégrés dans la page `stats.html` à l’aide de balises `<canvas>` et de scripts JavaScript.

---

### 23.5 Intégration dans l’interface

- Ajout d’un lien **Stats** dans la barre de navigation
- Mise en page responsive avec Bootstrap
- Les graphes sont affichés côte à côte pour une meilleure lisibilité

---

### 23.6 Résultat

Cette extension permet de transformer l’application en un véritable outil d’analyse naturaliste :

- La carte montre _où_ les observations ont lieu
- Les statistiques expliquent _quoi_ et _quand_ elles ont été observées
- L’ensemble offre une vision claire, structurée et exploitable des données

## Question 23 — 
### Partie d'implémentation du journal personnel

Cette partie décrit l'implémentation technique de l'extension permettant à chaque utilisateur de consulter uniquement ses propres observations dans une page dédiée appelée **Mon journal**. Cette fonctionnalité s'appuie sur le champ `owner` ajouté au modèle et sur les permissions déjà mises en place dans les questions précédentes.

---

## 1. Mise à jour du modèle

Un champ `owner` a été ajouté au modèle `Observation` afin d'associer chaque observation à l'utilisateur qui l'a créée :

```python
owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
```

Ce champ est utilisé exclusivement pour l'extension du journal personnel.

---

## 2. Mise à jour de la vue de création d'observation

Lors de la création d'une observation, l'utilisateur connecté est automatiquement enregistré comme propriétaire :

```python
if form.is_valid():
    observation = form.save(commit=False)
    observation.utilisateur = request.user   
    observation.owner = request.user         
    observation.save()
```

pour que chaque observation est correctement liée à son créateur.

---

## 3. Création de la vue `mon_journal`

Une nouvelle vue a été ajoutée pour afficher uniquement les observations appartenant à l'utilisateur connecté :

```python
@login_required
def mon_journal(request):
    observations = Observation.objects.filter(owner=request.user).order_by('-date')
    return render(request, 'observo/mon_journal.html', {
        'observations': observations
    })
```

---

## 4. Ajout de l'URL associée

Dans `observo/urls.py` :

```python
path('mon_journal/', views.mon_journal, name='mon_journal'),
```

---

## 5. Création du template `mon_journal.html`

Le template affiche les observations de l'utilisateur sous forme de tableau .


## 6. Mise à jour de la barre de navigation

Un lien vers le journal personnel a été ajouté dans `base.html`, visible uniquement pour les utilisateurs connectés :

```html
<li class="nav-item">
    <a class="nav-link" href="{% url 'mon_journal' %}">Mon journal</a>
</li>
```

---
## 7. Tests réalisés

- Aprés la création d'une observation , cette derniere apparaît immédiatement dans Mon journal.
- toutes les autres pages fonctionnent toujours comme avant.

