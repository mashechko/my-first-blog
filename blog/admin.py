from django.contrib import admin
from .models import Post, News, Category, Author


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'published_date')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'link')
    search_fields = ('title', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', )
    search_fields = ('name', )


admin.site.register(Post, PostAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author)