from django.urls import path
from books.views import BookListView, BookListApiView

app_name = "books"
urlpatterns = [
    path("books/", BookListView.as_view(), name="books-list"),
    path("api/books/", BookListApiView.as_view(), name="books-api-list"),
]
