from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),  # Use hyphens for improved URL readability
    path('profile/<str:username>/', views.profilepage, name='profile_page'),  # Renamed URL pattern
]