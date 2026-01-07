from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'observo/about.html')

from django.shortcuts import render, get_object_or_404
from .models import Animal

def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, 'observo/animal_detail.html', {'animal': animal})
