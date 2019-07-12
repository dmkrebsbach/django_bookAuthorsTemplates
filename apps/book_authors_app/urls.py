from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^books$', views.books),
    url(r'^books/create$', views.createBook),
    url(r'^books/(?P<bookId>\d+)$', views.showBook),
    url(r'^books/(?P<bookId>\d+)/update$', views.updateBook),
    url(r'^books/(?P<bookId>\d+)/edit$', views.editBook),

    url(r'^authors$', views.authors),
    url(r'^authors/create$', views.createAuthor),
    url(r'^authors/(?P<authorId>\d+)$', views.showAuthor),
    url(r'^authors/(?P<authorId>\d+)/update$', views.updateAuthor),
    url(r'^authors/(?P<authorId>\d+)/edit$', views.editAuthor),
]