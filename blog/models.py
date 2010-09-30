from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify

class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.email)

class Post(models.Model):
    title        = models.CharField(max_length=64)
    slug         = models.SlugField(unique_for_date='date')
    author       = models.ForeignKey(Author)
    body         = models.TextField(blank=True)
    tease        = models.TextField(blank=True, 
        help_text='A brief description of the post.')
    published_on = models.DateField(auto_now_add=True)    
    
    def __unicode__(self):
        return "%s (%s)" % (self.title, self.author.name)    

