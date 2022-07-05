
from django.urls import path
from .views import *


urlpatterns = [
    path('', landing, name='landing'),
    path('about', about, name='about'),
    path('blogs', blogs, name='blogs'),
    path('blogs/detail/<int:id>', blogs_detail, name='blogs_detail'),
    # muveqqeti
    path('job-posting', job_posting, name='job-posting'),
    path('job-single/<int:id>', job_single, name='job-single'),

    path('store', store, name='store'),
    path('store-single/<int:id>', store_single, name='store-single'),
    path('<slug:category_slug>/',
         store_by_category, name='store_by_category'),

    path('privacy-policy', privacy_policy, name='privacy-policy'),
    path('terms-conditions', terms_conditions, name='terms-conditions'),


]
