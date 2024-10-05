from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.models import User

def profile(request):
    # Логика для отображения профиля текущего пользователя
    user = request.user
    context = {'user': user}
    return render(request, 'templates/profile.html', context)

def profile_detail(request, user_id):
    # Логика для отображения профиля конкретного пользователя
    user = get_object_or_404(User, pk=user_id)
    context = {'user': user}
    return render(request, 'templates/profile_detail.html', context)