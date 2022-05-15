
from django.urls import path
from .views import *


urlpatterns = [
    path('', landing, name='landing'),
    path('about', about, name='about'),
    path('job-posting', job_posting, name='job-posting'),
    path('blogs', blogs, name='blogs'),
    path('blogs/detail/<int:id>', blogs_detail, name='blogs_detail'),


]
