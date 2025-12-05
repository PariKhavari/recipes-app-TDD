from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from recipes_app.models import Recipe


class BaseRecipeAPITestCase(APITestCase):
    """
    Base test class that provides shared setup and helper methods
    for the Recipe API tests.
    """

    def setUp(self):
        """
        Runs before each test method.
        Creates a default user, token and stores commonly used URLs.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
        )

        self.token = Token.objects.create(user=self.user)

        self.list_url = reverse("recipes-list")

    def authenticate(self):
        """
        Attach the token to the HTTP Authorization header for authenticated requests.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def create_recipe(self, author=None, title="Test-Rezept", description="Beschreibung"):
        """
        Helper method to create a Recipe instance for tests.
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
    Unhappy path tests: requests without valid authentication.
    """

    def test_post_recipe_without_auth_returns_401(self):
        """
        POST without authentication should return 401 Unauthorized
        and must NOT create a recipe.
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
        GET /recipes-detail/<id>/ without authentication should return 401 Unauthorized.
        """
        recipe = self.create_recipe()

        detail_url = reverse("recipes-detail", kwargs={"pk": recipe.id})

        response = self.client.get(detail_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class RecipeAPITestCaseHappy(BaseRecipeAPITestCase):
    """
    Happy path tests: requests with valid authentication.
    """

    def test_get_recipes_list_with_auth_returns_200_and_empty_list(self):
        """
        As an authenticated user, GET /recipes-list/ should return 200 OK
        and an empty list when no recipes exist.
        """
        self.authenticate()
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_post_recipe_with_auth_returns_201_and_creates_recipe(self):
        """
        As an authenticated user, POST to /recipes-list/ should create a recipe
        and return 201 Created.
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
        As an authenticated user, GET /recipes-detail/<id>/ should return 200 OK
        and the correct recipe data.
        """
        recipe = self.create_recipe()

        detail_url = reverse("recipes-detail", kwargs={"pk": recipe.id})

        self.authenticate()
        response = self.client.get(detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], recipe.id)
        self.assertEqual(response.data["title"], recipe.title)

    def test_recipe_str_returns_title(self):
        """
        __str__ of Recipe should return the title.
        """
        recipe = self.create_recipe(title="My Test Recipe")
        self.assertEqual(str(recipe), "My Test Recipe")