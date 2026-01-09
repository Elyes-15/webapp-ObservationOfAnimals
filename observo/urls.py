from django.contrib import admin
from django.urls import path
from observo import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('about/', views.about, name='about'),


    path('observs/<int:id>/', views.detail_observation, name='detail_observation'),
    path('observs/', views.liste_observations, name='liste_observations'),
    path('new_observ/', views.new_observ, name='new_observ'),
    path('delete_observ/<int:id>/', views.delete_observ, name='delete_observ'),
    path('change_observ/<int:id>/', views.change_observ, name='change_observ'),

    path('animals/<int:animal_id>/', views.animal_detail, name='animal_detail'),
    path('animals/', views.animal_list, name='animal_list'),
    path('new_animal/', views.new_animal, name='new_animal'),
    path('delete_animal/<int:animal_id>/',
         views.delete_animal, name='delete_animal'),
    path('change_animal/<int:animal_id>/',
         views.change_animal, name='change_animal'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('stats/', views.stats_view, name='stats'),
     path('mon_journal/', views.mon_journal, name='mon_journal'),
       path('admin-required/', views.admin_required_page, name='admin_required'),
]
