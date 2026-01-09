#Tests des modèles
from django.test import TestCase
from .models import Animal, Observation
from django.contrib.auth.models import User
from django.urls import reverse
class TestModeleAnimal(TestCase):
    def test_creation_animal(self):
        animal = Animal.objects.create(
            nom_commun="Renard",
            description="Animal sauvage"
        )
        self.assertEqual(animal.nom_commun, "Renard")


class TestVuesAnimaux(TestCase):

    def test_page_liste_animaux(self):
        response = self.client.get(reverse("animal_list"))
        self.assertEqual(response.status_code, 200)



class TestObservations(TestCase):

    def setUp(self):
        self.utilisateur = User.objects.create_user(
            username="test2026",
            password="motdepasse"
        )

    def test_acces_page_observations(self):
        self.client.login(username="test2026", password="motdepasse")
        response = self.client.get(reverse("liste_observations"))
        self.assertEqual(response.status_code, 200)



    def test_page_inscription_existe(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)








