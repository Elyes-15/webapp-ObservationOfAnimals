from observo.models import Animal, Observation
from datetime import date, time
import random

animals = list(Animal.objects.all())

for i in range(50):
    Observation.objects.create(
        date=date(2024, random.randint(1, 12), random.randint(1, 28)),
        heure=time(random.randint(0, 23), random.randint(0, 59)),
        latitude=48 + random.random(),
        longitude=2 + random.random(),
        animal=random.choice(animals),
        description=f"Observation automatique numero {i+1}"
    )

print("50 observations crees.")
