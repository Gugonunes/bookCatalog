from django.shortcuts import render

# Create your views here.


def wishlist_page(request):
    return render(request, 'wishlist/index.html')
