# cc2/urls.py
from django.contrib import admin
from django.urls import path
from observo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
     path('animals/<int:animal_id>/', views.animal_detail, name='animal_detail'),
      path('animals/', views.animal_list, name='animal_list'),
]
