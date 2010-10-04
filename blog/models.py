import re
from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from django.contrib.sitemaps import Sitemap

class Blog(models.Model):
    name = models.CharField(max_length=64)
    base_url = models.CharField('Base URL', max_length=200,
        help_text='Example: With base URL "personal" your blog posts would '
                  'be below /blog/personal/...<br />'
                  'Slashes ("/") are not allowed in this field.')
    description = models.CharField(max_length=500, blank=True,
        help_text='This will also be your feed description')

    def __unicode__(self):
        return "%s" % (self.name)
    
    @models.permalink
    def get_absolute_url(self):
        return ('blog.views.show', (), {'blog_url': self.base_url})

class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.email)

def default_blog():
    blogs = Blog.objects.all()[:1]
    if blogs:
        return blogs[0]
    return None

class Post(models.Model):
    blog = models.ForeignKey(Blog, related_name='posts',
        default=default_blog,
        help_text="Changing the blog will also change the post's URL, so "
                  "better don't change it for a published post.")
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique_for_date='date_published')
    author = models.ForeignKey(Author)
    body = models.TextField(blank=True)
    date_published = models.DateTimeField()
    date_modified = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        if not self.date_published:
            self.published_on = datetime.now()
        elif self.date_published:
            self.date_modified = datetime.now()
        super(Post, self).save(*args, **kwargs)       

    @models.permalink 
    def get_absolute_url(self):
        return ('blog.views.show', (), {'post_url': self.slug, 
                'year': self.date_published.year,
                'month': '%02d' % self.date_published.month}) 
    
    class Meta:
        ordering = ["-date_published"]

    def __unicode__(self):
        return "%s" % (self.title,)

class PostsSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return Post.objects.filter().order_by('-date_published')[:2000]

    def lastmod(self, obj):
        return obj.last_update
