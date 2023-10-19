from django.contrib import admin
from my_news.models import CategoryModel, NewsModel

# Register your models here.


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


