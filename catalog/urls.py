from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    # path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    # path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    # URL conf for on loan books
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    # challenge: page only visible for librarians, that displays all books that have been borrowed, and which includes the name of each borrower
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
]
