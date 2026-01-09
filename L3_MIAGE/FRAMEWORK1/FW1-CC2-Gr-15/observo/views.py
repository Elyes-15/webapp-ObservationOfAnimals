from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from .models import Observation, Animal, Profile
from .forms import ObservationForm, AnimalForm, CustomAuthenticationForm, SimpleUserCreationForm
from django.contrib.auth.models import User



def est_admin(user):
    """Vérifie si l'utilisateur est administrateur."""
    if not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    try:
        return user.profile.role == 'admin'
    except (Profile.DoesNotExist, AttributeError):
        create_profile_if_missing(user)
        return False

def peut_modifier_observation(user, observation):
    """Vérifie si l'utilisateur peut modifier/supprimer une observation."""
    if not user.is_authenticated:
        return False
    if est_admin(user):
        return True
    return observation.utilisateur == user if observation.utilisateur else False

def create_profile_if_missing(user):
    """Crée un profil pour un utilisateur s'il n'en a pas."""
    try:
        return Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return Profile.objects.create(user=user, role='user')



def about(request):
    return render(request, 'observo/about.html')



def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'observo/animal_list.html', {'animals': animals})

def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, 'observo/animal_detail.html', {'animal': animal})

@user_passes_test(est_admin)
def new_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Animal ajouté avec succès !")
            return redirect('animal_list')
    else:
        form = AnimalForm()
    return render(request, 'observo/new_animal.html', {'form': form})

@user_passes_test(est_admin)
def change_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, "Animal modifié avec succès !")
            return redirect('animal_list')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'observo/change_animal.html', {'form': form, 'animal': animal})

@user_passes_test(est_admin)
def delete_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    if request.method == 'POST':
        animal.delete()
        messages.success(request, "Animal supprimé avec succès !")
        return redirect('animal_list')
    return render(request, 'observo/delete_animal.html', {'animal': animal})



@login_required
def liste_observations(request):
    """Affiche toutes les observations."""
    if est_admin(request.user):
        observations = Observation.objects.all().order_by('-date', '-heure')
    else:
        observations = Observation.objects.filter(utilisateur=request.user).order_by('-date', '-heure')
    return render(request, 'observo/liste_observations.html', {'observations': observations})

@login_required
def detail_observation(request, id):
    observation = get_object_or_404(Observation, pk=id)
    if not peut_modifier_observation(request.user, observation):
        raise PermissionDenied("Vous n'avez pas accès à cette observation.")
    return render(request, 'observo/detail_observation.html', {'observation': observation})

@login_required
def new_observ(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            messages.success(request, "Observation ajoutée avec succès !")
            return redirect('liste_observations') 
    else:
        form = ObservationForm()
    return render(request, 'observo/new_observ.html', {'form': form})

@login_required
def change_observ(request, id):
    observation = get_object_or_404(Observation, pk=id)
    if not peut_modifier_observation(request.user, observation):
        raise PermissionDenied("Vous ne pouvez pas modifier cette observation.")
    if request.method == 'POST':
        form = ObservationForm(request.POST, instance=observation)
        if form.is_valid():
            form.save()
            messages.success(request, "Observation modifiée avec succès !")
            return redirect('liste_observations')  
    else:
        form = ObservationForm(instance=observation)
    return render(request, 'observo/change_observ.html', {'form': form, 'observation': observation})

@login_required
def delete_observ(request, id):
    observation = get_object_or_404(Observation, pk=id)
    if not peut_modifier_observation(request.user, observation):
        raise PermissionDenied("Vous ne pouvez pas supprimer cette observation.")
    if request.method == 'POST':
        observation.delete()
        messages.success(request, "Observation supprimée avec succès !")
        return redirect('liste_observations')  
    return render(request, 'observo/delete_observ.html', {'observation': observation})



def register_view(request):
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Compte créé avec succès !')
            return redirect('animal_list')
    else:
        form = SimpleUserCreationForm()
    return render(request, 'observo/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bienvenue {user.username} !')
            return redirect('animal_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'observo/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect('animal_list')


@login_required
def liste_observations(request):
    """Affiche toutes les observations et la barre de filtre par animal."""
    if est_admin(request.user):
        observations = Observation.objects.all().order_by('-date', '-heure')
    else:
        observations = Observation.objects.filter(utilisateur=request.user).order_by('-date', '-heure')
    
  
    animaux = Animal.objects.all().order_by('nom_commun')

    return render(request, 'observo/liste_observations.html', {
        'observations': observations,
        'animaux': animaux, 
    })

