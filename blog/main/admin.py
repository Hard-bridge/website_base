from django.contrib import admin
from .models import Book, Author, News, View, User

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(News)
admin.site.register(View)
admin.site.register(User)