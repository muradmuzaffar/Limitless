from random import choices
from secrets import choice
from statistics import mode
from django.db import models
from django.urls import reverse

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.first_name


class Subscribtion(models.Model):
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, null=True, unique=True)

    def __str__(self):
        return self.name


class Blogs(models.Model):
    user = models.ForeignKey('auth.User',  on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    describtion = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


TYPE_CHOICES = [
    ("full time", ("full time")),
    ("part time", ("part time")),
    ("freelance", ("freelance")),
    ("remote", ("remote"))

]


class Jobs(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    salaryByDefault = models.BooleanField(blank=True, null=True, default=False)
    dedline = models.DateField()
    about = models.TextField()
    requirements = models.TextField()

    def __str__(self):
        return self.name


SIZE_CHOICES = [
    ("X", ("X")),
    ("M", ("M")),
    ("XL", ("XL")),
    ("Yoxdur", ("Yoxdur")),

]

COLOR_CHOICES = [
    ("Ağ", ("Ağ")),
    ("Qara", ("Qara")),
    ("Mavi", ("Mavi")),
    ("Qırmızı", ("Qırmızı")),
    ("Sarı", ("Sarı")),
    ("Bənövşəyi", ("Bənövşəyi")),
    ("Qarışıq", ("Qarışıq")),


]


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, null=True, unique=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(blank=True, null=True)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    about = models.TextField()
    image1 = models.ImageField()
    image2 = models.ImageField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)
    image4 = models.ImageField(blank=True, null=True)
    image5 = models.ImageField(blank=True, null=True)
    # category = models.CharField(
    #     max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name
