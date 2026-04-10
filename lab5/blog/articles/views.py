#coding:utf-8
from django.shortcuts import render, redirect
from django.http import Http404
from .models import Article

def archive(request):
    posts = Article.objects.all()
    return render(request, 'archive.html', {'posts': posts})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {'post': post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    # Если пользователь не авторизован, возвращаем 404 (как в методичке)
    if not request.user.is_authenticated():
        raise Http404

    if request.method == "POST":
        # Собираем данные из формы
        title = request.POST.get("title", "").strip()
        text = request.POST.get("text", "").strip()
        errors = []

        # Проверка на пустые поля
        if not title:
            errors.append("Введите название статьи")
        if not text:
            errors.append("Введите текст статьи")

        # Проверка на уникальность названия (доп. задание)
        if title and Article.objects.filter(title=title).exists():
            errors.append("Статья с таким названием уже существует")

        if not errors:
            # Создаём новую статью
            article = Article.objects.create(
                title=title,
                text=text,
                author=request.user
            )
            # Перенаправляем на страницу новой статьи
            return redirect('get_article', article_id=article.id)

        # Если есть ошибки, передаём их в шаблон
        return render(request, 'create_post.html', {
            'title': title,
            'text': text,
            'errors': errors,
        })
    else:
        # GET-запрос – просто показываем пустую форму
        return render(request, 'create_post.html')