from django.contrib import admin
from ingredients.models import (
    Category,
    Ingredient
)

class CategoryAdmin(admin.ModelAdmin):
    pass

class IngredientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)