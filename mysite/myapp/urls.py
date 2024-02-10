from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.indexItem, name="detail"),
    path('additem/', views.add_item, name="add_item"),
    path('updateitem/<int:id>/', views.update_item, name="update_item"),
    path('deleteitem/<int:id>/', views.delete_item, name="delete_item"),
]
