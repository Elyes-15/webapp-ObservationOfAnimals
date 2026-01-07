from django.shortcuts import render , get_object_or_404
from .models import Observation

# Create your views here.
def about(request):
    return render(request, 'observo/about.html')


def detail_observation(request, id):
    observation = get_object_or_404(Observation, pk=id)
    return render(request, 'observo/detail_observation.html', {'observation': observation})

def liste_observations(request):
    observations = Observation.objects.all().order_by('-date', '-heure')
    return render(request, 'observo/liste_observations.html', {'observations': observations})