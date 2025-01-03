from django.db import models
from users.models import User
from books.models import Book
# Create your models here.


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    books = models.ManyToManyField(Book, related_name='wishlist')

    def __str__(self):
        return f"Lista de desejos de {self.user.username}"
