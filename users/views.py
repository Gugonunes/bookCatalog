from django.shortcuts import render
from users.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def user_page(request):
    user = request.user
    return render(request, 'users/index.html', {'user': user})

