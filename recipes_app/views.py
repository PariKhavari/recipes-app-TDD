from django.shortcuts import render
from rest_framework import viewsets, permissions, authentication
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    Vollständiges CRUD-ViewSet für Rezepte.
    (Auth & Permissions fügen wir später hinzu.)
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
