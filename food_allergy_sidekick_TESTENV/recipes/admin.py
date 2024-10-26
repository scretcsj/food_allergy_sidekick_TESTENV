from django.contrib import admin
from .models import Recipe, KeyValueStore


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'ingredients', 'instructions')

admin.site.register(Recipe, RecipeAdmin)


class KeyValueStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'strmeal', 'strcategory', 'strinstructions')

admin.site.register(KeyValueStore, KeyValueStoreAdmin)