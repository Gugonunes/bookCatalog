from django.shortcuts import render

# Create your views here.


def reviews_home(request):
    return render(request, 'reviews/index.html')
