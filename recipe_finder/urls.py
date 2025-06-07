from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page showing pantry and add/delete/search functionality
    path('results/', views.results, name='results'),  # Results page showing matching recipes
]
