from django.urls import path
from books.views import BookListView, BookView, BookListApiView, BookApiView

app_name = "books"
urlpatterns = [
    path("books/", BookListView.as_view(), name="books-list"),
    path("books/<int:book_id>/", BookView.as_view(), name="book"),
    path("api/books/", BookListApiView.as_view(), name="books-api-list"),
    path("api/books/<int:book_id>/", BookApiView.as_view(), name="api-book"),
]
