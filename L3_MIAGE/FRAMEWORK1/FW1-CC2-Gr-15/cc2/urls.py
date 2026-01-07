from django.contrib import admin
from django.urls import path, include
from observo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about, name='home'), 
    path('about/', views.about, name='about'),
    path('', include('observo.urls')),
]
