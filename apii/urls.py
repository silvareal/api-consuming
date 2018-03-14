from django.urls import path
from . import views

urlpatterns = [
    path('map', views.home, name='map'),
    path('github', views.github, name='github'),
    path('dictionary', views.oxford, name='dictionary')
]