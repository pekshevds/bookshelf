from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse, HttpRequest, HttpResponse
from books.models import Book
from books.utils import convert_object, convert_objects


class BookListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        books = Book.objects.all()
        return render(
            request, "books/index.html", {"books": books, "title": "Наша библиотека"}
        )


class BookView(View):
    def get(self, request: HttpRequest, book_id: int) -> HttpResponse:
        book = get_object_or_404(Book, id=book_id)
        return render(request, "books/book.html", {"book": book, "title": book.title})


class BookListApiView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        books = Book.objects.all()
        return JsonResponse(convert_objects(books), safe=False)


class BookApiView(View):
    def get(self, request: HttpRequest, book_id: int) -> HttpResponse:
        book = get_object_or_404(Book, id=book_id)
        return JsonResponse(convert_object(book), safe=False)
