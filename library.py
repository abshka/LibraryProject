import json
from typing import List, Dict, Union


class Library:
    def __init__(self, storage_path: str = "storage.json"):
        self.storage_path = storage_path
        self.books = self._load_books()

    def _load_books(self) -> List[Dict]:
        """Загружает книги из JSON-файла."""
        try:
            with open(self.storage_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_books(self) -> None:
        """Сохраняет книги в JSON-файл."""
        with open(self.storage_path, "w", encoding='utf-8') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title: str, author: str, year: int) -> Dict:
        """Добавляет новую книгу в библиотеку."""
        book = {
            "id": len(self.books) + 1,
            "title": title,
            "author": author,
            "year": year,
            "status": "в наличии",
        }
        self.books.append(book)
        self._save_books()
        return book

    def delete_book(self, book_id: int) -> bool:
        """Удаляет книгу по ID."""
        for book in self.books:
            if book["id"] == book_id:
                self.books.remove(book)
                self._save_books()
                return True
        return False

    def search_books(self, key: str, value: Union[str, int]) -> List[Dict]:
        """Ищет книги по указанному полю."""
        return [book for book in self.books if str(book.get(key)) == str(value)]

    def list_books(self) -> List[Dict]:
        """Возвращает список всех книг."""
        return self.books

    def update_status(self, book_id: int, status: str) -> bool:
        """Обновляет статус книги."""
        if status not in ["в наличии", "выдана"]:
            raise ValueError("Неверный статус! Доступны только 'в наличии' или 'выдана'.")
        for book in self.books:
            if book["id"] == book_id:
                book["status"] = status
                self._save_books()
                return True
        return False

    @staticmethod
    def format_book(book: Dict) -> str:
        """Возвращает форматированный текст для отображения книги."""
        return (
            f"ID: {book['id']}\n"
            f"Название: {book['title']}\n"
            f"Автор: {book['author']}\n"
            f"Год издания: {book['year']}\n"
            f"Статус: {book['status']}\n"
            f"************"
        )
