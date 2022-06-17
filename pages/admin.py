from django.contrib import admin

# Register your models here.
from .models import Contact, Blogs, Category,Jobs


admin.site.register(Contact)
admin.site.register(Blogs)
admin.site.register(Jobs)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
