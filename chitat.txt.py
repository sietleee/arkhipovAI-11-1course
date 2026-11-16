books = []

while True:
    print("\n=== ЧИТАТЕЛЬСКИЙ ДНЕВНИК ===")
    print("1 - Добавить книгу")
    print("2 - Показать все книги")
    print("3 - Показать последние 5 прочитанных")
    print("4 - Заменить название по номеру")
    print("5 - Поиск по названию")
    print("6 - Статистика")
    print("0 - Выход")

    choice = input("Выберите пункт меню: ").strip()

    if choice == "1":
        name = input("Введите название книги: ").strip()

        if name:
            books.append(name)
            print("Книга добавлена!")
        else:
            print("Ошибка: название не может быть пустым.")

    elif choice == "2":
        if not books:
            print("Дневник пуст.")
        else:
            print("\nСписок прочитанных книг:")
            for i, book in enumerate(books, start=1):
                print(f"{i}. {book}")

    elif choice == "3":
        if not books:
            print("Дневник пуст.")
        else:
            print("\nПоследние прочитанные книги:")
            for i, book in enumerate(books[-5:],
                                   start=max(1, len(books) - 4)):
                print(f"{i}. {book}")

    elif choice == "4":
        number = input("Введите номер книги: ").strip()

        if number.isdigit():
            number = int(number)

            if 1 <= number <= len(books):
                new_name = input("Введите новое название: ").strip()

                if new_name:
                    books[number - 1] = new_name
                    print("Название успешно изменено!")
                else:
                    print("Ошибка: название не может быть пустым.")
            else:
                print("Ошибка: книги с таким номером нет.")
        else:
            print("Ошибка: введите положительное число.")

    elif choice == "5":
        if not books:
            print("Дневник пуст.")
        else:
            search = input("Введите слово для поиска: ").strip().lower()

            if search:
                found = False

                for i, book in enumerate(books, start=1):
                    if search in book.lower():
                        print(f"{i}. {book}")
                        found = True

                if not found:
                    print("Ничего не найдено.")
            else:
                print("Ошибка: поисковый запрос пуст.")

    elif choice == "6":
        if not books:
            print("Дневник пуст.")
        else:
            print("\n=== СТАТИСТИКА ===")
            print(f"Всего прочитано книг: {len(books)}")
            print(f"Первая книга: {books[0]}")
            print(f"Последняя книга: {books[-1]}")

    elif choice == "0":
        print("Спасибо за использование читательского дневника!")
        break

    else:
        print("Ошибка: выберите пункт от 0 до 6.")