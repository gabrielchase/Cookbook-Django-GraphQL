import graphene

from graphene_django.types import DjangoObjectType

from cookbook.ingredients.models import (
    Category,
    Ingredient
)

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient


class Query(graphene.AbstractType):
    all_categories = graphene.List(CategoryType)
    all_ingredients = graphene.List(IngredientType)

    def resolve_all_categories(self, args, context, info):
        return Category.objects.all()

    def resolve_all_ingredients(self, args, context, info):
        return Ingredient.objects.select_related('category').all()