from django.shortcuts import render, get_object_or_404, redirect
from .models import Observation, Animal, Profile
from .forms import ObservationForm, AnimalForm, CustomAuthenticationForm, SimpleUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.contrib import messages


def est_admin(user):
    """Vérifie si l'utilisateur est administrateur."""
    if not user.is_authenticated:
        return False
    # Vérifie d'abord si c'est un superuser Django
    if user.is_superuser:
        return True
    # Ensuite vérifie le rôle dans le profil
    try:
        return user.profile.role == 'admin'
    except (Profile.DoesNotExist, AttributeError):
        # Crée un profil par défaut si manquant
        create_profile_if_missing(user)
        return False


def peut_modifier_observation(user, observation):
    """Vérifie si l'utilisateur peut modifier/supprimer une observation."""
    if not user.is_authenticated:
        return False
    if est_admin(user):
        return True
    return observation.utilisateur == user if observation.utilisateur else False


def about(request):
    return render(request, 'observo/about.html')


@login_required
def detail_observation(request, id):
    observation = get_object_or_404(Observation, pk=id)
    if not peut_modifier_observation(request.user, observation):
        raise PermissionDenied("Vous n'avez pas accès à cette observation.")
    return render(request, 'observo/detail_observation.html', {'observation': observation})


@login_required
def liste_observations(request):
    if est_admin(request.user):
        observations = Observation.objects.all().order_by('-date', '-heure')
    else:
        observations = Observation.objects.filter(
            utilisateur=request.user).order_by('-date', '-heure')
    return render(request, 'observo/liste_observations.html', {'observations': observations})


@login_required
def new_observ(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST)
        if form.is_valid():
            # Passez l'utilisateur connecté au formulaire
            observation = form.save(commit=False, user=request.user)
            observation.utilisateur = request.user
            observation.save()
            return redirect('liste_observations')
    else:
        form = ObservationForm()

    return render(request, 'observo/new_observ.html', {'form': form})


@login_required
def delete_observ(request, id):
    observation = get_object_or_404(Observation, pk=id)

    # Vérification des permissions AVANT toute action
    if not peut_modifier_observation(request.user, observation):
        raise PermissionDenied(
            "Vous ne pouvez pas supprimer cette observation.")

    if request.method == 'POST':
        observation.delete()
        return redirect('liste_observations')

    return render(request, 'observo/delete_observ.html', {'observation': observation})


@login_required
def change_observ(request, id):
    observation = get_object_or_404(Observation, pk=id)
    if not peut_modifier_observation(request.user, observation):
        raise PermissionDenied(
            "Vous ne pouvez pas modifier cette observation.")

    if request.method == 'POST':
        form = ObservationForm(request.POST, instance=observation)
        if form.is_valid():
            form.save()
            return redirect('liste_observations')
    else:
        form = ObservationForm(instance=observation)

    return render(request, 'observo/change_observ.html', {'form': form, 'observation': observation})


def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, 'observo/animal_detail.html', {'animal': animal})


def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'observo/animal_list.html', {'animals': animals})


@user_passes_test(est_admin)
def new_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm()

    return render(request, 'observo/new_animal.html', {'form': form})


@user_passes_test(est_admin)
def delete_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    if request.method == 'POST':
        animal.delete()
        return redirect('animal_list')

    return render(request, 'observo/delete_animal.html', {'animal': animal})


@user_passes_test(est_admin)
def change_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)

    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm(instance=animal)

    return render(request, 'observo/change_animal.html', {
        'form': form,
        'animal': animal
    })


def register_view(request):
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            try:
                # 1. Crée l'utilisateur SANS profil
                user = form.save()

                # 2. Crée le profil MANUELLEMENT avec get_or_create
                Profile.objects.get_or_create(
                    user=user,
                    defaults={'role': form.cleaned_data['role']}
                )

                # 3. Connecte l'utilisateur
                login(request, user)
                messages.success(request, 'Compte créé avec succès !')
                return redirect('animal_list')

            except IntegrityError as e:
                # Gestion spécifique de l'erreur d'intégrité
                messages.error(request, f"Erreur de base de données: {str(e)}")
                return render(request, 'observo/register.html', {'form': form})

            except Exception as e:
                # Gestion des autres erreurs
                messages.error(request, f"Erreur inattendue: {str(e)}")
                return render(request, 'observo/register.html', {'form': form})
    else:
        form = SimpleUserCreationForm()
    return render(request, 'observo/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenue {username}!')
                next_url = request.GET.get('next', 'animal_list')
                return redirect(next_url)
            else:
                messages.error(
                    request, "Nom d'utilisateur ou mot de passe incorrect.")
        else:
            messages.error(
                request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'observo/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect('animal_list')


def create_profile_if_missing(user):
    """Crée un profil pour un utilisateur s'il n'en a pas."""
    try:
        profile = Profile.objects.get(user=user)
        return profile
    except Profile.DoesNotExist:
        # Crée un profil par défaut avec rôle 'user'
        profile = Profile.objects.create(user=user, role='user')
        return profile


@login_required
def debug_profile(request):
    """Vue de débogage pour vérifier les profils."""
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
        role = profile.role
        created = False
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user, role='user')
        role = profile.role
        created = True

    return render(request, 'observo/debug_profile.html', {
        'user': user,
        'profile': profile,
        'role': role,
        'created': created,
    })
