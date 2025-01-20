from django.shortcuts import render
from books.models import Book
from reviews.models import Review
from reviews.utils import find_reviews_by_book_name


# Create your views here.


def reviews_home(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = find_reviews_by_book_name(book.title)

    content = {
        'book': book,
        'reviews': reviews
    }
    return render(request, 'reviews/index.html', context=content)
