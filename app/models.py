from django.db import models

# Create your models here.

class Author(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)

class Topic(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)

class Book(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ManyToManyField(Topic, null=True, blank=True)

class Tag(models.Model):
    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return ('id__iexact', 'name__icontains',)
    name = models.CharField(max_length=255)

class Quote(models.Model):
    def __str__(self):
        return '%s...' % self.text[:100]
    text = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ManyToManyField(Tag, null=True, blank=True)
    approved = models.BooleanField(default=False)
    published = models.BooleanField(default=False)