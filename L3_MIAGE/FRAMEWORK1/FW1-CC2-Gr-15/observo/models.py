from django.db import models

class Animal(models.Model):
    nom_commun = models.CharField(max_length=100)
    nom_savant = models.CharField(max_length=100)
    embranchement = models.CharField(max_length=50)
    classe = models.CharField(max_length=50)
    ordre = models.CharField(max_length=50)
    sous_ordre = models.CharField(max_length=50, blank=True, null=True)
    famille = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
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
