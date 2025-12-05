from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from recipes_app.models import Recipe

class RecipeAPITestCaseHappy(APITestCase):
    """
    Happy-Path-Tests für die Recipe-API.
    """

    def test_get_recipes_list_returns_200(self):
        """
        Der Endpunkt /recipes-list/ soll 200 OK liefern,
        auch wenn noch keine Rezepte existieren.
        """
        url = reverse("recipes-list")  # entspricht /recipes-list/
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # optional: prüfen, dass eine Liste zurückkommt
        self.assertEqual(response.data, [])



    def test_post_recipe_creates_recipe_and_returns_201(self):
        """
        Ein POST auf /recipes-list/ soll ein Rezept mit Status 201 Created erzeugen.
        Author wird im Test explizit gesetzt.
        """
        url = reverse("recipes-list")
        author = User.objects.create_user(username="author", password="test1234")

        payload = {
            "title": "Test-Rezept",
            "description": "Sehr leckeres Testrezept.",
            "author": author.id,  # wir übergeben die User-ID
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)
        recipe = Recipe.objects.first()
        self.assertEqual(recipe.title, "Test-Rezept")
        self.assertEqual(recipe.author, author)



















# from django.urls import reverse
# from rest_framework.test import APITestCase, APIClient
# from rest_framework import status
# # from .models import Question
# # from forum_app.api.serializers import QuestionSerializer
# from django.contrib.auth.models import User


# class LikeTests(APITestCase):
#     def test_create_account(self):
#         url = 'http://127.0.0.1:8000/api/forum/likes/'
#         response = self.client.get(url)
#         # self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
     
     
# class QuestionTests(APITestCase):

#     def setUp(self):
#         self.user= User.objects.create_user(username='testuser', password='testpassword')
#         # self.question = Question.objects.create(title='TestQuestion', content='Testcontent', author=self.user, category='frontend')
#         self.client = APIClient()
#         self.client.login(username='testuser', password='testpassword')



#     def test_list_post_question(self):
#         url = reverse('question-list')
#         # beim create: self.user, beim post:self.user.id
#         data = {'title':'Question',
#                 'content':'1Content',
#                 'author':self.user.id,
#                 'category':'frontend'}
#         # self.client.logout()
#         response = self.client.post(url, data, format="json")
       
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


#     def test_detail_question(self):
#         url = reverse('question-detail', kwargs={'pk':self.question.id})
#         response = self.client.get(url)
#         # expected_data = QuestionSerializer(self.question).data
        





#         # 4 wichtige Test Methoden
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # self.assertEqual(response.data,expected_data)
#         self.assertDictEqual(response.data, expected_data)
#         self.assertJSONEqual(response.content, expected_data)
#         self.assertContains(response, 'title')
     
  