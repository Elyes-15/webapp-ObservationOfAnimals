from django.db import models

class Animal(models.Model):
    nom_commun = models.CharField(max_length=100)
    nom_savant = models.CharField(max_length=200)
    embranchement = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    ordre = models.CharField(max_length=100)
    sous_ordre = models.CharField(max_length=100)
    famille = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    statut_iucn = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.nom_commun


class Observation(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Observation de {self.animal.nom_commun} le {self.date}"
