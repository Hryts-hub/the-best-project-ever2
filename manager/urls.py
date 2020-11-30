from django.urls import path
from manager.views import hello, book_hello

urlpatterns = [
    path('hello/', hello),
    path('book_hello/', book_hello),
]