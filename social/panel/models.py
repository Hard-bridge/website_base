from django.db import models
class User(models.Model):
    fio = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default=None)
    phone = models.CharField(max_length=200, default=None)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.login

class Category(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class New(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/', default='news/defailt.png')
    created_at = models.DateTimeField(auto_now=True)
    count_like = models.IntegerField(default=0)

    def __str__(self):
        return self.title

