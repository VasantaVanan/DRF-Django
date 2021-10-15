from django.contrib import admin
from . import models


@admin.register(models.Blog)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Title', 'id', 'author')

admin.site.register(models.Category)