from django.db import models


class Book(models.Model):
    book_name = models.JSONField(default=dict)
    author_name = models.CharField(max_length=255, null=True, blank=True)
    published_date = models.DateField(auto_now=True)