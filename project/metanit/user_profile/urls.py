from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('<int:user_id>/', views.profile_detail, name='profile_detail'),
]
