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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    bio = models.TextField()
    favorite = models.ManyToManyField('RecipeItem', symmetrical=False, blank=True,related_name='favorite')

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    description = models.TextField()
    prep_time = models.CharField(max_length=50)
    instructions = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.author.name}"
