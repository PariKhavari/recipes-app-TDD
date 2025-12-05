from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

router = DefaultRouter()
# WICHTIG:
# prefix="recipes-list" erzeugt /recipes-list/
# basename="recipes" erzeugt URL-Namen recipes-list & recipes-detail
router.register("recipes-list", RecipeViewSet, basename="recipes")

urlpatterns = [
    path("", include(router.urls)),
]
