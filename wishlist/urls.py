from django.urls import path
from wishlist import views as wishlist_views

app_name = 'home_wishlist'

urlpatterns = [
    path('', wishlist_views.wishlist_page, name='wishlist_page')
]