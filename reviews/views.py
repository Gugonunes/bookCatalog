from django.shortcuts import render
from books.models import Book
from reviews.models import Review
# Create your views here.

def find_reviews_by_book_name(book_name):
    book = Book.objects.get(title=book_name)
    reviews = Review.objects.filter(book=book)
    return reviews

def reviews_home(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = find_reviews_by_book_name(book.title)

    content = {
        'book': book,
        'reviews': reviews
    }
    return render(request, 'reviews/index.html', context=content)
