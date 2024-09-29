import pytest
from django.test import TestCase
from books.models import Book


@pytest.mark.django_db
def test_books_with_the_same_authors():
    books_count = 5
    author_full_name = "some author"
    for i in range(books_count):
        Book.objects.create(
            title=f"title{i}",
            author_full_name=author_full_name,
            year_of_publishing=2020,
            copies_printed=200,
            short_description="",
        )
    assert Book.objects.filter(author_full_name=author_full_name).count() == books_count


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
