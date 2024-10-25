from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'ingredients', 'instructions')

admin.site.register(Recipe, RecipeAdmin)
