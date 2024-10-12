from django.contrib import admin
from .models import Article
from django.contrib import admin

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
 list_display = ['title', 'slug', 'author', 'publish', 'status']
 list_filter = ['status', 'created', 'publish', 'author']
 search_fields = ['title', 'body']
 prepopulated_fields = {'slug': ('title',)}
 raw_id_fields = ['author']
 date_hierarchy = 'publish'
 ordering = ['status', 'publish']
 show_facets = admin.ShowFacets.ALWAYS

# admin.site.register(Article)