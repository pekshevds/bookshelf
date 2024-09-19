from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpRequest, HttpResponse
from books.models import Book


class BookListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        books = Book.objects.all()
        return render(request, "books/index.html", {"books": books})


class BookListApiView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        books = Book.objects.all().values()
        return JsonResponse(list(books), safe=False)
