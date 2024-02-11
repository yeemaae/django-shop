from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

from .views import MyLoginView

app_name = "users"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', MyLoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('sellerprofile/<int:id>/', views.seller_profile, name='sellerprofile'),
]

