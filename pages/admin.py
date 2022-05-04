from django.contrib import admin

# Register your models here.
from .models import Contact, Blogs, Category


admin.site.register(Contact)
admin.site.register(Blogs)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
