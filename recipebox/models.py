""" 
Author
    Name

NewsItem
    Date
    Title 
    Body
    author
 """
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class NewsItem(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    date=models.DateTimeField()


    def __str__(self):
        return f"{self.title} - {self.author.name}"