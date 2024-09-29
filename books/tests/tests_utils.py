from django.test import TestCase
from books.models import Book
from books.utils import ObjectToDictConverter, ObjectsListToDictConverter


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
