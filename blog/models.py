import re
from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify

class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.email)

class Post(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique_for_date='date_published')
    author = models.ForeignKey(Author)
    body = models.TextField(blank=True)
    date_published = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % (self.title,)

    @models.permalink
    def get_absolute_url(self):
        return ('blog.views.show', (), {'post_url': self.slug, 
                'year': self.date_published.year,
                'month': '%02d' % self.date_published.month})

    def get_tag_list(self):
        return re.split(" ", self.tags,)    
    
    class Meta:
        ordering = ["-date_published"]

