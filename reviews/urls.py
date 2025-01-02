from django.urls import path
from reviews import views as reviews_views

app_name = 'home'

urlpatterns = [
    path('', reviews_views.reviews_home, name='reviews_home'),
]
