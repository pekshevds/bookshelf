from django.test import TestCase
from books.models import Book


class TestViewsBook(TestCase):
    def setUp(self) -> None:
        self.book = Book.objects.create(
            title="book1",
            author_full_name="author1",
            year_of_publishing=2020,
            copies_printed=1000,
            short_description="some description",
        )

    def test__book_list_view__success(self) -> None:
        result = self.client.get("/books/")
        self.assertTrue(result.status_code == 200)

    def test__book_list_view__not_success(self) -> None:
        result = self.client.get("/books~xxx/")
        self.assertTrue(result.status_code != 200)

    def test__book_view__success(self) -> None:
        result = self.client.get(f"/books/{self.book.id}/")
        self.assertTrue(result.status_code == 200)

    def test__book_view__not_success(self) -> None:
        result = self.client.get(f"/books/{self.book.id + 1}/")
        self.assertTrue(result.status_code != 200)

    def test__book_list_api_view__success(self) -> None:
        result = self.client.get("/api/books/")
        self.assertTrue(result.status_code == 200)

    def test__book_list_api_view__not_success(self) -> None:
        result = self.client.get("/api/books~xxx/")
        self.assertTrue(result.status_code != 200)

    def test__book_api_view__success(self) -> None:
        result = self.client.get(f"/api/books/{self.book.id}/")
        self.assertTrue(result.status_code == 200)

    def test__book_api_view__not_success(self) -> None:
        result = self.client.get(f"/api/books/{self.book.id + 1}/")
        self.assertTrue(result.status_code != 200)

    def test__book_list_api_view__result_isnt_empty(self) -> None:
        result = self.client.get(f"/api/books/{self.book.id}/")
        self.assertTrue(len(result.json()) > 0)
