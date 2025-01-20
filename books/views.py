from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from django.conf.urls.static import static

from reviews.utils import find_reviews_by_book_name


# Create your views here.


def books_home(request):
    all_books = Book.objects.all()

    content = {
        'books': all_books
    }
    return render(request, 'books/index.html', context=content)


def unique_book(request, book_id):
    book = Book.objects.get(id=book_id)
    title = book.title
    image = book.cover_image
    author = book.author.name
    categories = book.categories
    synopsis = book.synopsis

    reviews = find_reviews_by_book_name(book.title)

    content = {
        'title': title,
        'image': image,
        'author': author,
        'categories': categories,
        'synopsis': synopsis,
        'reviews': reviews
    }

    return render(request, 'books/unique_book.html', context=content)

