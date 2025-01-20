from django.urls import path
from books import views as book_views

app_name = 'home_books'

urlpatterns = [
    path('', book_views.books_home, name='books_home'),
    path('<int:book_id>', book_views.unique_book, name='unique_book')
]
