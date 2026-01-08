from django import forms
from django.core.validators import MinValueValidator
from .models import Observation

class ObservationForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    heure = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    latitude = forms.FloatField(validators=[MinValueValidator(0)])
    longitude = forms.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        model = Observation
        fields = ['animal', 'date', 'heure', 'latitude', 'longitude', 'description']
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'nom_commun',
            'nom_savant',
            'embranchement',
            'classe',
            'ordre',
            'sous_ordre',
            'famille',
            'genre',
            'statut_iucn',
            'description',
        ]
