from django.urls import path
from books import views as book_views

app_name = 'home'

urlpatterns = [
    path('', book_views.home, name='home'),
]
