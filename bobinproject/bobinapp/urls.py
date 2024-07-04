from django.urls import path
from. import views

urlpatterns = [
    path('', views.index),
    path('index', views.index, name="index"),
    path('onlinebook', views.onlinebook, name="onlinebook"),
    path('delete1/<int:id>', views.delete1, name="delete1"),
    path('edit/<int:id>', views.edit, name="edit"),
    
]