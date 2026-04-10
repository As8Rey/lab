#coding:utf-8
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
    
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        password2 = request.POST.get('password2', '').strip()
        errors = []

        # Валидация
        if not username:
            errors.append('Имя пользователя обязательно')
        elif User.objects.filter(username=username).exists():
            errors.append('Пользователь с таким именем уже существует')

        if password != password2:
            errors.append('Пароли не совпадают')
        elif len(password) < 4:
            errors.append('Пароль должен содержать не менее 4 символов')

        if not errors:
            # Создаём пользователя
            user = User.objects.create_user(username, email, password)
            # Сразу авторизуем после регистрации
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('archive')   # на главную

        # Если ошибки – показываем форму с ошибками
        return render(request, 'registration.html', {
            'username': username,
            'email': email,
            'errors': errors,
        })
    else:
        return render(request, 'registration.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        errors = []

        if not username or not password:
            errors.append('Введите имя пользователя и пароль')
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Перенаправляем на страницу, с которой пришли, или на главную
                next_url = request.GET.get('next', 'archive')
                return redirect(next_url)
            else:
                errors.append('Неверное имя пользователя или пароль')

        return render(request, 'login.html', {'errors': errors, 'username': username})
    else:
        return render(request, 'login.html')
def user_logout(request):
    logout(request)
    return redirect('archive')