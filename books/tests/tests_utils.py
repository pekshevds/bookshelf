import pytest
from django.test import TestCase
from books.models import Book
from books.utils import (
    ObjectToDictConverter,
    ObjectsListToDictConverter,
    objects_fields,
    convert_object,
    convert_objects,
)


@pytest.fixture()
def book():
    book = Book.objects.create(
        **{
            "title": "book1",
            "author_full_name": "author1",
            "year_of_publishing": 2019,
            "copies_printed": 5000,
            "short_description": "some description1",
        }
    )
    return book


@pytest.fixture()
def book_in_a_dict():
    return {
        "id": 1,
        "title": "book1",
        "author_full_name": "author1",
        "year_of_publishing": 2019,
        "copies_printed": 5000,
        "short_description": "some description1",
    }


@pytest.fixture()
def book_fields():
    return [
        "id",
        "title",
        "author_full_name",
        "year_of_publishing",
        "copies_printed",
        "short_description",
    ]


@pytest.mark.django_db
def test__objects_fields__check_book_fields_equals_standard_fields(book, book_fields):
    fields = objects_fields(book)
    assert fields == book_fields


@pytest.mark.django_db
def test__objects_fields__check_book_fields_not_equals_standard_fields(
    book, book_fields
):
    fields = objects_fields(book)
    fields.pop(0)
    assert fields != book_fields


@pytest.mark.django_db
def test__convert_object__check_converted_book_equals_book_in_a_dict(
    book, book_in_a_dict
):
    assert convert_object(book) == book_in_a_dict


@pytest.mark.django_db
def test__convert_object__check_converted_book_contains_all_the_fields(
    book, book_in_a_dict
):
    book_dict = convert_object(book)
    assert len(book_dict) == len(book_in_a_dict)


@pytest.mark.django_db
def test__convert_object__check_fields_is_none(book, book_in_a_dict):
    book_dict = convert_object(book, fields=None)
    assert book_dict == book_in_a_dict


@pytest.mark.django_db
def test__convert_object__check_book_contains_fake_fields(book, book_in_a_dict):
    book_dict = convert_object(book, fields=["qwdfqw"])
    assert book_dict != book_in_a_dict


@pytest.mark.django_db
def test__convert_objects__check_converted_list_of_books_equals_books_in_a_list_of_dict(
    book, book_in_a_dict
):
    assert convert_objects([book]) == [book_in_a_dict]


@pytest.mark.django_db
def test__convert_objects__check_converted_list_of_books_not_equals_books_in_a_list_of_dict(
    book, book_in_a_dict
):
    fields = ["title"]
    assert convert_objects([book], fields) != [book_in_a_dict]


class TestUtils(TestCase):
    def setUp(self) -> None:
        self.book = Book.objects.create(
            title="book1",
            author_full_name="author1",
            year_of_publishing=2019,
            copies_printed=5000,
            short_description="some description1",
        )

    def test__object_to_dict_converter__is_exist(self) -> None:
        dict = ObjectToDictConverter(self.book).convert()
        self.assertEqual(dict.get("id"), 1)

    def test__object_list_to_dict_converter_consist_three_elements(self) -> None:
        Book.objects.create(
            title="book2",
            author_full_name="author5",
            year_of_publishing=2020,
            copies_printed=333,
            short_description="some description2",
        )
        Book.objects.create(
            title="book3",
            author_full_name="author2",
            year_of_publishing=2022,
            copies_printed=100,
            short_description="some description3",
        )
        list = ObjectsListToDictConverter(Book.objects.all()).convert()
        self.assertEqual(len(list), 3)
