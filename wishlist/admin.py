from django.contrib import admin
from wishlist.models import Wishlist

# Register your models here.


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['list_books']

    def list_books(self, obj):
        books = obj.books.order_by('title')
        return ', '.join([book.title for book in books])


admin.site.register(Wishlist, WishlistAdmin)
