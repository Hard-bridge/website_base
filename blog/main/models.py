from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='books/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news')
    create_at = models.DateTimeField(auto_now=True)

class View(models.Model):
    new = models.ForeignKey(News,  on_delete=models.CASCADE)
    count = models.IntegerField()

class User(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    fio = models.TextField()
