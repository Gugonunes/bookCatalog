from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def list_books(request):
    content = {
        'livros': [
            (1, 'O programador pragmático'),
            (2, 'DDD'),
            (3, 'Refatorando')
        ]
    }
    return render(request, 'index.html', context=content)
