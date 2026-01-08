from django.shortcuts import render, get_object_or_404, redirect
from .models import Observation
from .forms import ObservationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm, CustomAuthenticationForm
from .models import Profile

from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Animal
from .forms import AnimalForm
# Create your views here.


def about(request):
    return render(request, 'observo/about.html')


def detail_observation(request, id):
    observation = get_object_or_404(Observation, pk=id)
    return render(request, 'observo/detail_observation.html', {'observation': observation})


@login_required
def liste_observations(request):
    if request.user.profile.role == 'admin':
        observations = Observation.objects.all().order_by('-date', '-heure')
    else:
        observations = Observation.objects.all().order_by('-date', '-heure')
    return render(request, 'observo/liste_observations.html', {'observations': observations})


def new_observ(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_observations')
    else:
        form = ObservationForm()

    return render(request, 'observo/new_observ.html', {'form': form})


def delete_observ(request, id):
    observation = get_object_or_404(Observation, pk=id)

    if request.method == 'POST':
        observation.delete()
        return redirect('liste_observations')

    return render(request, 'observo/delete_observ.html', {'observation': observation})


def change_observ(request, id):
    observation = get_object_or_404(Observation, pk=id)

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


def new_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm()

    return render(request, 'observo/new_animal.html', {'form': form})


def delete_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    if request.method == 'POST':
        animal.delete()
        return redirect('animal_list')

    return render(request, 'observo/delete_animal.html', {'animal': animal})


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
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte créé pour {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
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
                return redirect('animal_list')
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
