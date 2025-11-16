from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name




