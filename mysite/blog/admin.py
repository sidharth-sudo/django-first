from django.contrib import admin
from . import models

# Register your models here. so you can access them on admin area


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author']

admin.site.register(models.Post, AuthorAdmin)
# admin.site.register(models.)
