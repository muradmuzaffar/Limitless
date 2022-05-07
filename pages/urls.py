
from django.urls import path
from .views import *


urlpatterns = [
    path('', landing, name='landing'),
    path('about', about, name='about'),
    path('blogs', blogs, name='blogs'),
    path('blogs/detail', blogs_detail, name='blogs_detail'),


]
