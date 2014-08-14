from django.db import models

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __unicode__(self):
        return self.tag

class Shareman(models.Model):
    man = models.CharField(max_length=30)

    def __unicode__(self):
        return self.man

    
class Book(models.Model):
    name = models.CharField(max_length=30)
    picaddress = models.CharField(max_length=50)
    download = models.CharField(max_length=80)
    douban = models.CharField(max_length=100)
    sharereason = models.CharField(max_length=100)
    booktag = models.ManyToManyField(Tag)
    bookman = models.ManyToManyField(Shareman)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.name

