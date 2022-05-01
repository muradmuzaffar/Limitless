
from django.urls import path
from .views import *


urlpatterns = [
    path('', landing, name='landing'),
    path('about', about, name='about'),


]
