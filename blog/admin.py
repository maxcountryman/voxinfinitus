from django.contrib import admin
from .models import Blog, Author, Post

class BlogAdmin(admin.ModelAdmin):
    list_disply = ('name', 'base_url', 'description',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'slug', 'author', 'body', 'date_published', 'tweet',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
