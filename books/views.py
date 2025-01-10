from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from django.conf.urls.static import static

# Create your views here.


def books_home(request):
    all_books = Book.objects.all()

    content = {
        'books': all_books
    }
    return render(request, 'books/index.html', context=content)
