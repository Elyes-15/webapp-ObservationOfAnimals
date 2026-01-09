from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Animal, Observation, Profile


class ObservationForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    heure = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})
    )
    latitude = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
        label="Latitude"
    )
    longitude = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
        label="Longitude"
    )

    class Meta:
        model = Observation
        fields = ['animal', 'date', 'heure', 'latitude', 'longitude', 'description']
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
        widgets = {
            'nom_commun': forms.TextInput(attrs={'class': 'form-control'}),
            'nom_savant': forms.TextInput(attrs={'class': 'form-control'}),
            'embranchement': forms.TextInput(attrs={'class': 'form-control'}),
            'classe': forms.TextInput(attrs={'class': 'form-control'}),
            'ordre': forms.TextInput(attrs={'class': 'form-control'}),
            'sous_ordre': forms.TextInput(attrs={'class': 'form-control'}),
            'famille': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'statut_iucn': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


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
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, initial='user', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.create(user=user, role=self.cleaned_data['role'])
        return user
