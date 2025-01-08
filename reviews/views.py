from django.shortcuts import render
from books.models import Book
from reviews.models import Review
# Create your views here.


def find_book_by_index(book_index):
    all_books = Book.objects.all()
    index = 0
    for book in all_books:
        index += 1
        if index == book_index:
            title = book.title
            author = book.author
            img_url = book.cover_image.url
            publication_date = book.publication_date
            categories = ", ".join(category.name for category in book.categories.all())
            synopsis = book.synopsis

            return {
                'index': index,
                'title': title,
                'author': author,
                'img_url': img_url,
                'publication_date': publication_date,
                'categories': categories,
                'synopsis': synopsis
            }
    return None

def find_reviews_by_book_name(book_name):
    book = Book.objects.get(title=book_name)
    reviews = Review.objects.filter(book=book)
    return reviews

def reviews_home(request, book_index):
    book = find_book_by_index(book_index)
    reviews = find_reviews_by_book_name(book['title'])

    content = {
        'book': book,
        'reviews': reviews
    }
    return render(request, 'reviews/index.html', context=content)
