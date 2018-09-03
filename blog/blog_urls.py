from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^article/edit/(?P<article_id>[0-9]+)$', views.article_edit_page, name='article_edit_page'),
    url(r'^article/edit/action$', views.article_edit_page_action, name='article_edit_page_action'),
    # url(r'^article/delete$', views.article_delete, name='article_delete')
]
