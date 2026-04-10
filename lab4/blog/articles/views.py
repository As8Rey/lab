# Create your views here.
#coding:utf-8
from django.shortcuts import render
from .models import Article   # или from models import Article
from django.http import Http404

def archive(request):
    posts = Article.objects.all()  # получаем все статьи из БД
    return render(request, 'archive.html', {'posts': posts})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
