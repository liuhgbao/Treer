from django.db import models

class Tag(models.Model):
	tag_name = models.CharField(max_length=20)
	create_time = models.DateTimeField(auto_now_add=True)

        def __unicode__(self):
            return self.tag_name


class Category(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name

class Language(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(blank=True)
	info = models.TextField()

	def __unicode__(self):
		return u'%s' % (self.name)

class Article(models.Model):
	caption = models.CharField(max_length=30)
	publish_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(Author)
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag, blank=True)
	content = models.TextField()

class Works(models.Model):
	caption = models.CharField(max_length=30)
	publish_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(Author)
	language = models.ForeignKey(Language)
	downloads = models.CharField(max_length=100)
	tags = models.ManyToManyField(Tag, blank=True)
	content = models.TextField()


# Create your models here.
