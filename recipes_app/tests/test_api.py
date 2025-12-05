from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from recipes_app.models import Recipe


class BaseRecipeAPITestCase(APITestCase):
    """
    Basisklasse, die gemeinsam genutzte Objekte bereitstellt.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
        )
        self.token = Token.objects.create(user=self.user)

        self.list_url = reverse("recipes-list")

    def authenticate(self):
        """
        Setzt das Token im Authorization-Header.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def create_recipe(self, author=None, title="Test-Rezept", description="Beschreibung"):
        """
        Hilfsfunktion, um ein Rezept in Tests anzulegen.
        """
        if author is None:
            author = self.user
        return Recipe.objects.create(
            title=title,
            description=description,
            author=author,
        )

