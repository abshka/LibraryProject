import unittest
from library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library(storage_path="test_storage.json")

    def tearDown(self):
        import os
        os.remove("test_storage.json")

    def test_add_book(self):
        book = self.library.add_book("Test Book", "Test Author", 2024)
        self.assertEqual(book["title"], "Test Book")

    def test_delete_book(self):
        self.library.add_book("Book to Delete", "Author", 2024)
        self.assertTrue(self.library.delete_book(1))
        self.assertFalse(self.library.delete_book(2))

    def test_search_books(self):
        self.library.add_book("Searchable Book", "Author", 2024)
        results = self.library.search_books("title", "Searchable Book")
        self.assertEqual(len(results), 1)

    def test_update_status(self):
        self.library.add_book("Status Book", "Author", 2024)
        self.assertTrue(self.library.update_status(1, "выдана"))
        self.assertEqual(self.library.books[0]["status"], "выдана")


if __name__ == '__main__':
    unittest.main()
