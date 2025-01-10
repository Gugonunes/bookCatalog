from django.shortcuts import render
from books.models import Book
from django.db.models import Avg

from reviews.models import Review

def get_top_rated_book():
    top_book = (
        Review.objects.values('book')
        .annotate(average_rating=Avg('rating'))
        .order_by('-average_rating')
        .first()
    )

    if top_book:
        book_id = top_book['book']

        best_book = Book.objects.get(id=book_id)
        return best_book
    else:
        return None

# Create your views here.
def home_view(request):
    top_book = get_top_rated_book()
    recent_reviews = Review.objects.order_by('-created_at')[:3]
    content = {
        'top_book': top_book,
        'recent_reviews': recent_reviews
    }
    return render(request, 'home/index.html', context=content)
