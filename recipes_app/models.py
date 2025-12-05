from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    """
    Simple recipe model.
    """
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

