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


class RecipeAPITestCaseUnhappy(BaseRecipeAPITestCase):
    """
    Unhappy-Path-Tests: ohne oder mit falscher Authentifizierung.
    """

    def test_post_recipe_without_auth_returns_401(self):
        """
        Ein POST ohne Authentifizierung soll 401 Unauthorized liefern.
        """
        payload = {
            "title": "Unerlaubtes Rezept",
            "description": "Soll nicht erstellt werden.",
            "author": self.user.id,
        }

        response = self.client.post(self.list_url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Recipe.objects.count(), 0)

    def test_get_recipe_detail_without_auth_returns_401(self):
        """
       Detailabruf ohne Auth gibt 401 Unauthorized.
        """
        recipe = self.create_recipe()

        detail_url = reverse("recipes-detail", kwargs={"pk": recipe.id})

        response = self.client.get(detail_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class RecipeAPITestCaseHappy(BaseRecipeAPITestCase):
    """
    Happy-Path-Tests: mit gültiger Authentifizierung.
    """

    def test_get_recipes_list_with_auth_returns_200_and_empty_list(self):
        """
        Als eingeloggter User soll GET /recipes-list/ 200 OK und eine Liste liefern.
        (zu diesem Zeitpunkt noch leer)
        """
        self.authenticate()
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_post_recipe_with_auth_returns_201_and_creates_recipe(self):
        """
       Als eingeloggter User ein Rezept erstellen (201 Created).
        """
        self.authenticate()

        payload = {
            "title": "Authentifiziertes Rezept",
            "description": "Nur für eingeloggte Nutzer.",
            "author": self.user.id,
        }

        response = self.client.post(self.list_url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)

        recipe = Recipe.objects.first()
        self.assertEqual(recipe.title, "Authentifiziertes Rezept")
        self.assertEqual(recipe.author, self.user)

    def test_get_recipe_detail_with_auth_returns_200(self):
        """
        Aufgabe 6: Rezept-Detail als eingeloggter User abrufen (200 OK).
        """
        recipe = self.create_recipe()

        detail_url = reverse("recipes-detail", kwargs={"pk": recipe.id})

        self.authenticate()
        response = self.client.get(detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], recipe.id)
        self.assertEqual(response.data["title"], recipe.title)
