from django.shortcuts import render
from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def article_edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/article_edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_edit_page.html', {'article': article})


def article_edit_page_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id_hidden', '0')
    # 保存数据
    # 如果是零则create，否则save
    if str(article_id) == '0':
        models.Article.objects.create(title=title, content=content)
        # 数据保存完成返回首页
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})


# def article_delete(request):
#     article_id = request.POST.get('article_id_hidden', '0')  # 获取此文的id
#     article = models.Article.objects.get(pk=article_id)
#     article.delete()
#     return render(request, 'blog/index.html')
