from django.contrib import admin
from blog.models import Author, Post

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'slug', 'author', 'body', 'tease',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
