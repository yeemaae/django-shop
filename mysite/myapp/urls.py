from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index),

    path('<int:id>/', views.indexItem, name="detail"),
]
