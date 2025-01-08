from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from django.conf.urls.static import static

# Create your views here.


def books_home(request):
    all_books = Book.objects.all()
    books_list = []
    index = 0
    for book in all_books:
        index += 1
        title = book.title
        author = book.author
        img_url = book.cover_image.url
        publication_date = book.publication_date
        categories = ", ".join(category.name for category in book.categories.all())
        synopsis = book.synopsis

        books_list.append({
            'index': index,
            'title': title,
            'author': author,
            'img_url': img_url,
            'publication_date': publication_date,
            'categories': categories,
            'synopsis': synopsis
        })

    content = {
        'books': books_list
    }
    return render(request, 'books/index.html', context=content)
