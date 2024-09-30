import pytest
from django.test import TestCase
from django.db.utils import IntegrityError
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
def test_create_various_books_names_with_the_same_authors():
    books_count = 2
    author_full_name = "author1"
    for i in range(books_count):
        Book.objects.create(
            title=f"title{i}",
            author_full_name=author_full_name,
            year_of_publishing=2020,
            copies_printed=200,
            short_description="",
        )
    assert Book.objects.filter(author_full_name=author_full_name).count() == books_count


@pytest.mark.django_db
def test_create_the_same_books_names_with_various_authors():
    books_count = 2
    title = "book1"
    for i in range(books_count):
        Book.objects.create(
            title=title,
            author_full_name=f"author{i}",
            year_of_publishing=2020,
            copies_printed=200,
            short_description="",
        )
    assert Book.objects.filter(title=title).count() == books_count


@pytest.mark.django_db
def test_tryes_to_create_the_same_books_with_one_author(book):
    Book.objects.create(**book)
    with pytest.raises(IntegrityError):
        Book.objects.create(**book)


class TestBook(TestCase):
    def setUp(self) -> None:
        pass

    def test__create_book(self) -> None:
        book = Book.objects.create(
            title="book1",
            author_full_name="author1",
            year_of_publishing=2020,
            copies_printed=1000,
            short_description="some description",
        )
        self.assertEqual(book.id, 1)

    def test__fetch_book(self) -> None:
        book_id: int = 1
        Book.objects.create(
            title="book1",
            author_full_name="author1",
            year_of_publishing=2020,
            copies_printed=1000,
            short_description="some description",
        )
        self.assertIsNotNone(Book.objects.filter(id=book_id).first())
