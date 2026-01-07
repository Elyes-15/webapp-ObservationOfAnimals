# cc2/urls.py
from django.contrib import admin
from django.urls import path
from observo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('observs/<int:id>/', views.detail_observation, name='detail_observation'),
    path('observs/', views.liste_observations, name='liste_observations'),
    path('new_observ/', views.new_observ, name='new_observ'),


]
