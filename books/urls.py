from django.conf.urls import url

from books import views

urlpatterns = [
  url(r'^$', views.BookList.as_view(), name='book_list'),
  url(r'^(?P<pk>\d+)$', views.BookDetail.as_view(), name='book_detail'),
  url(r'^new$', views.BookCreate.as_view(), name='book_new'),
  url(r'^edit/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
]
