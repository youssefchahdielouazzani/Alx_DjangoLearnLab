from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    published_year = models.IntegerField()

    def __str__(self):
        return self.title



