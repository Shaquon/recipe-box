""" 
Author
    Name

RecipeItem
    Title
    Author (ForeignKey)
    Description
    Time Required
    Instructions (`TextField`)
 """

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, default="empty")
    bio = models.TextField()

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    title = models.CharField(max_length=50, default="empty")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    prep_time = models.CharField(max_length=50, default="empty")
    instructions = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.author.name}"
