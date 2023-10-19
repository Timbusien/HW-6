from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Категории новостей'
        verbose_name_plural = 'Добавить Категории новостей'


class NewsModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='news_images')
    descriptions = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Добавить новосит'
        verbose_name_plural = 'Добавить новости тут'

