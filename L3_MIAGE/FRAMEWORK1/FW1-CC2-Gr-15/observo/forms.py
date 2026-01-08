from .models import Animal
from django import forms
from django.core.validators import MinValueValidator
from .models import Observation, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


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


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmation du mot de passe', widget=forms.PasswordInput)
    role = forms.ChoiceField(
        label='Rôle', choices=Profile.ROLE_CHOICES, initial='user')

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Les mots de passe ne correspondent pas.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            # Crée le profil associé
            Profile.objects.create(user=user, role=self.cleaned_data['role'])
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
