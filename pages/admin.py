from django.contrib import admin

# Register your models here.
from .models import Contact, Blogs, Category, Jobs, Products, ProductCategory, Subscribtion


admin.site.register(Contact)
admin.site.register(Blogs)
admin.site.register(Jobs)
admin.site.register(Products)
admin.site.register(Subscribtion)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
