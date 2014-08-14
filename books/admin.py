from django.contrib import admin
from books.models import Book,Tag,Shareman
# Register your models here.

admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Shareman)
