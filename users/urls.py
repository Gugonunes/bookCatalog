from django.urls import path
from users import views as users_views

app_name = 'home'

urlpatterns = [
    path('', users_views.user_page, name='user_page')
]