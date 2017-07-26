import graphene

from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField

from ingredients.models import (
    Category,
    Ingredient
)

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (graphene.Node,)


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['icontains'],
            'category__name': ['exact']
        }
        interfaces = (graphene.Node,)


class Query(graphene.AbstractType):
    ingredient = graphene.Field(
        IngredientType, 
        id=graphene.ID(), 
        name=graphene.String()
    )

    category = graphene.Field(
        CategoryType,
        id=graphene.Int(),
        name=graphene.String()
    )
    
    all_categories = DjangoFilterConnectionField(CategoryType)
    all_ingredients = DjangoFilterConnectionField(IngredientType)

    def resolve_category(self, args, context, info):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)

        return None

    def resolve_all_categories(self, args, context, info):
        return Category.objects.all()

    def resolve_ingredient(self, args, context, info):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return Ingredient.objects.get(pk=id)

        if name is not None:
            return Ingredient.objects.get(name=name)

        return None

    def resolve_all_ingredients(self, args, context, info):
        return Ingredient.objects.select_related('category').all()