from django.shortcuts import render
from my_news.models import CategoryModel, NewsModel
from django.views.generic import TemplateView, ListView
# Create your views here.


class HomeTemplate(ListView):
    template_name = 'index.html'
    queryset = CategoryModel.objects.all()
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = NewsModel.objects.all()

        return context


class NewsTemplate(ListView):
    template_name = 'news.html'
    queryset = NewsModel.objects.all()
    context_object_name = 'news'

