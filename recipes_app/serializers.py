from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Recipe model.
    """

    class Meta:
        model = Recipe
        fields = ["id", "title", "description", "created_at", "author"]
