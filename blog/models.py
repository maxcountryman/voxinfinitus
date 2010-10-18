import utils
from django import template
from django.db import models
from django.conf import settings
from django.contrib.sitemaps import ping_google, Sitemap
from django.template.defaultfilters import slugify
from datetime import datetime
from taggit.managers import TaggableManager

class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.email)

class Blog(models.Model):
    name = models.CharField(max_length=64)
    base_url = models.CharField('Base URL', max_length=200,
        help_text='Example: With base URL "personal" your blog posts would '
                  'be below /blog/personal/...<br />'
                  'Slashes ("/") are not allowed in this field.')
    description = models.CharField(max_length=500, blank=True,
        help_text='Used for meta info in our HTML')

    def __unicode__(self):
        return "%s" % (self.name)
    
    @models.permalink
    def get_absolute_url(self):
        return ('blog.views.show', (), {'blog_url': self.base_url})

def default_blog():
    blogs = Blog.objects.all()[:1]
    if blogs:
        return blogs[0]
    return None

class Post(models.Model):
    blog = models.ForeignKey(Blog, related_name='posts',
        default=default_blog,
        help_text='Changing this will affect URIs!')
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique_for_date='date_published')
    author = models.ForeignKey(Author)
    body = models.TextField(blank=True)
    date_published = models.DateTimeField(auto_now_add=True)    
    is_published = models.BooleanField('Published', help_text='Mark here to publish',)
    is_modified = models.BooleanField(default=False)
    tags = TaggableManager()
    tweet = models.BooleanField('Tweet', help_text='Mark here to Tweet',)  
    
    def save(self, *args, **kwargs):
        if self.date_published is None:
            self.date_published = datetime.now() #if the date isn't set it needs to be set now or get_absolute_url() breaks
        if self.is_published is True and self.is_modified is False and self.tweet is True:
            absolute_url = settings.SITE_URL + self.get_absolute_url()
            utils.tweet(self.title.encode(), absolute_url)
            self.is_modified = True
        super(Post, self).save(*args, **kwargs)
        try:
             ping_google(sitemap_url='/sitemap.xml')
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass
        
    @models.permalink 
    def get_absolute_url(self):
        return ('blog.views.show', (), {'post_url': self.slug, 
                'blog_url': self.blog.base_url,
                'year': self.date_published.year,
                'month': '%02d' % self.date_published.month}) 
    
    class Meta:
        ordering = ["-date_published"]

    def __unicode__(self):
        return "%s" % (self.title,)

class PostsSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return Post.objects.filter().order_by('-date_published')[:50]

    def lastmod(self, obj):
        return obj.date_modified


