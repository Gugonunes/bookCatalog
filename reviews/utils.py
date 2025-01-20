from django.shortcuts import render
from books.models import Book
from reviews.models import Review
# Create your views here.


def find_reviews_by_book_name(book_name):
    book = Book.objects.get(title=book_name)
    reviews = Review.objects.filter(book=book)
    return reviews
