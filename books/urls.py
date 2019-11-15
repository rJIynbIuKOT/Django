from django.urls import path
from books.views import index
from . import views

urlpatterns = [
    path('', index),
    path('book/<int:pk>/', views.book_page, name='book_page'),
    path('book/new/', views.book_new, name='book_new'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/delete/<int:pk>/', views.delete, name='delete'),
]