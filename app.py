from library import Library


def main():
    library = Library()
    while True:
        print(
            "\n--- Меню ---\n"
            "1. Добавить книгу\n"
            "2. Удалить книгу\n"
            "3. Искать книгу\n"
            "4. Список всех книг\n"
            "5. Изменить статус книги\n"
            "0. Выход\n"
        )

        choice = input("Введите номер операции: ")
        try:
            match choice:
                case "1":
                    title = input("Введите название книги: ")
                    author = input("Введите автора книги: ")
                    year = int(input("Введите год издания: "))
                    book = library.add_book(title, author, year)
                    print("Книга добавлена:")
                    print(library.format_book(book))

                case "2":
                    book_id = int(input("Введите ID книги для удаления: "))
                    if library.delete_book(book_id):
                        print("Книга успешно удалена.")
                    else:
                        print("Книга с указанным ID не найдена.")

                case "3":
                    key = input("Введите поле для поиска (title/author/year): ")
                    value = input("Введите значение для поиска: ")
                    if key == "year":
                        value = int(value)
                    books = library.search_books(key, value)
                    if books:
                        print("Найденные книги:")
                        for book in books:
                            print(library.format_book(book))
                    else:
                        print("Книги не найдены.")

                case "4":
                    books = library.list_books()
                    if books:
                        print("Список книг:")
                        for book in books:
                            print(library.format_book(book))
                    else:
                        print("Библиотека пуста.")

                case "5":
                    book_id = int(input("Введите ID книги: "))
                    status = input("Введите новый статус (в наличии/выдана): ")
                    if library.update_status(book_id, status):
                        print("Статус книги успешно обновлен.")
                    else:
                        print("Книга с указанным ID не найдена.")

                case "0":
                    print("Выход из программы.")
                    exit()

                case _:
                    print("Некорректный ввод, попробуйте снова.")


        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
