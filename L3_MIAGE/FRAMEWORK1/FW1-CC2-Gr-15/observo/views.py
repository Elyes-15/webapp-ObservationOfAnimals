from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Animal
from .forms import AnimalForm
# Create your views here.
def about(request):
    return render(request, 'observo/about.html')


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