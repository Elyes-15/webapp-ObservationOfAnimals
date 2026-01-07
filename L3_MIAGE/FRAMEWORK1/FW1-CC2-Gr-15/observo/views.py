from django.shortcuts import render , get_object_or_404 , redirect
from .models import Observation
from .forms import ObservationForm

# Create your views here.
def about(request):
    return render(request, 'observo/about.html')


def detail_observation(request, id):
    observation = get_object_or_404(Observation, pk=id)
    return render(request, 'observo/detail_observation.html', {'observation': observation})

def liste_observations(request):
    observations = Observation.objects.all().order_by('-date', '-heure')
    return render(request, 'observo/liste_observations.html', {'observations': observations})



def new_observ(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_observations')  # renvoie vers la liste
    else:
        form = ObservationForm()

    return render(request, 'observo/new_observ.html', {'form': form})


def delete_observ(request, id):
    observation = get_object_or_404(Observation, pk=id)

    if request.method == 'POST':
        observation.delete()
        return redirect('liste_observations')

    return render(request, 'observo/delete_observ.html', {'observation': observation})

