from django.shortcuts import render
from rest_framework import viewsets, permissions, authentication
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    Full CRUD ViewSet for Recipe model.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]



