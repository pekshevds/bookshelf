import pytest
from django.test import TestCase
from django.urls import reverse
from books.models import Book


@pytest.fixture()
def book():
    return {
        "title": "book1",
        "author_full_name": "author1",
        "year_of_publishing": 2019,
        "copies_printed": 5000,
        "short_description": "some description1",
    }


@pytest.mark.django_db
def test__book_list_view__checks_route_books_list_is_calling(client):
    url = reverse("books:books-list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test__book_list_view__checks_finding_some_book_by_id_200(client, book):
    new_book = Book.objects.create(**book)
    url = reverse("books:book", kwargs={"book_id": new_book.id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test__book_list_view__checks_finding_some_book_by_id_404(client):
    url = reverse("books:book", kwargs={"book_id": 1})
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test__book_list_view__checks_route_books_api_list_is_calling(client):
    url = reverse("books:books-api-list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test__book_list_api_view__checks_the_result_contents_several_books(client, book):
    Book.objects.create(**book)
    url = reverse("books:books-api-list")
    response = client.get(url)
    data = response.json()
    assert len(data) >= 1


@pytest.mark.django_db
def test__book_list_api_view__checks_finding_some_book_by_id_200(client, book):
    new_book = Book.objects.create(**book)
    url = reverse("books:api-book", kwargs={"book_id": new_book.id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test__book_list_api_view__checks_finding_some_book_by_id_404(client, book):
    url = reverse("books:api-book", kwargs={"book_id": 1})
    response = client.get(url)
    assert response.status_code == 404


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
