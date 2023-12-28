from django.urls import path,include
from . import views

urlpatterns = [
    path('aboutus/',views.about,name='aboutus')
]
