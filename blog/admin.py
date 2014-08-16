#coding=utf-8
#感谢www.dannysite.com
from django.contrib import admin
from blog.models import Tag, Author, Article, Category , Works ,Language , Var

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name','email','info')
	search_fiels = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('caption', 'category', 'author', 'publish_time', 'update_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)


class WorksAdmin(admin.ModelAdmin):
    list_display = ('caption','language','author','publish_time','update_time','downloads')
    list_filter = ('publish_time',)
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)


class VarAdmin(admin.ModelAdmin):
    list_display = ('title','var','publish_time')
    list_filter = ('publish_time',)



admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Works, WorksAdmin)
admin.site.register(Language)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Var, VarAdmin)
# Register your models here.
