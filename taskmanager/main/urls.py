from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about_bitches', views.about, name='about'),
    path('create', views.create, name='create')
]