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


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, initial='user')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError(
                "Les mots de passe ne correspondent pas")

        # Vérifie si l'username existe déjà
        username = cleaned_data.get("username")
        from django.contrib.auth.models import User
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ce nom d'utilisateur existe déjà")

        return cleaned_data

    def save(self):
        from django.contrib.auth.models import User
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        role = self.cleaned_data['role']

        # Crée l'utilisateur
        user = User.objects.create_user(username, email, password)

        # Crée le profil
        Profile.objects.create(user=user, role=role)

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
