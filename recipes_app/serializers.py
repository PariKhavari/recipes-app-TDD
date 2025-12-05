from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer für das Recipe-Modell.
    """

    class Meta:
        model = Recipe
        fields = ["id", "title", "description", "created_at", "author"]
