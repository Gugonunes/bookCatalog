from django.contrib import admin
from books.models import Book, Author, Category
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['title']
    filter_horizontal = ['categories']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
