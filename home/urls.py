from django.urls import path
from home import views as home_views

app_name = 'home_view'

urlpatterns = [
    path('', home_views.home_view, name='home_view'),
]