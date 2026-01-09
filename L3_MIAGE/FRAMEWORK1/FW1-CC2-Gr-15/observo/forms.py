from django import forms
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Animal, Observation, Profile


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
        fields = ['animal', 'date', 'heure',
                  'latitude', 'longitude', 'description']
        exclude = ['utilisateur']

    def save(self, commit=True, user=None):
        observation = super().save(commit=False)
        if user:
            observation.utilisateur = user
        if commit:
            observation.save()
        return observation


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


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class SimpleUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, initial='user')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            # Crée le profil
            Profile.objects.create(user=user, role=self.cleaned_data['role'])

        return user
