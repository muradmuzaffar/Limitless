
from django.urls import path
from .views import *


urlpatterns = [
    path('', landing, name='landing'),
    path('about', about, name='about'),
    path('blogs', blogs, name='blogs'),
    path('blogs/detail/<int:id>', blogs_detail, name='blogs_detail'),
# muveqqeti
    path('job-posting', job_posting, name='job-posting'),
    path('job-single', job_single, name='job-single'),

]
