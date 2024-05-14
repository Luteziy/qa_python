**Финальный проект 4 спринта автоматизации**
=
<u>Приложение BookCollector позволяет:</u>


- Добавить книгу в список
- Установить жанр книги
- Отсортировать книги по жанрам (взрослые, детские)
- Добавить книгу в избранное
- Удалить книгу из списка избраного

<u>Для покрытия тестами приложения BooksCollector использовались методы</u>

- _add_new_book_ — добавляет новую книгу в словарь без указания жанра. Название книги может содержать максимум 40 символов. Одну и ту же книгу можно добавить только один раз.
- _set_book_genre_  — устанавливает жанр книги, если книга есть в books_genre и её жанр входит в список genre.
- _get_book_genre_ — выводит жанр книги по её имени.
- _get_books_with_specific_genre_ — выводит список книг с определённым жанром.
- _get_books_genre_ — выводит текущий словарь books_genre.
- _get_books_for_children_ — возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга.
- _add_book_in_favorites_ — добавляет книгу в избранное. Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя.
- _delete_book_from_favorites_ — удаляет книгу из избранного, если она там есть.
- _get_list_of_favorites_books_ — получает список избранных книг.


| **Метод** | **Название теста**                                                  | **Проверка метода**          |
|--------|---------------------------------------------------------------------|-------------------------------------------------------|
|add_new_book| 1. проверяем, что добавилось именно две                             | test_add_new_book_add_two_diferent_books              |
|add_new_book| 2. Добавление книги 40 символов в названии                          | test_add_new_book_with_namelen_more_40                |
| add_new_book| 3. Можно ли добавить 2 одинаковых книги                             | test_add_new_book_add_two_books_same_name             |
| set_book_genre| 4. Устанавливаем жанр книги                                         | test_set_book_genre                                   |
|get_book_genre| 5. Добавление книги в жанр по имени                                 | test_get_books_genre_add_new_book_with_no_genre       |
| get_books_with_specific_genre| 6 Выводим список книг с определённым жанром                         | test_get_books_with_specific_genre                    |
|set_book_genre | 7. Жанр книги не выводится, если его нет в books_genre              | test_set_book_genre_no_genre_not_in_books_genre       |
| get_books_for_children| 8. возвращаем книги, подходящие детям                               | test_get_books_for_children                           |
|get_books_for_children | 9. Книги с возрастным рейтингом отсутствуют в списке книг для детей | test_get_books_for_children_no_adult_genre            |
| add_book_in_favorites| 10. Добавляет книгу в избранное                                     | test_add_book_in_favorites_and_list_is_empty          |
| add_book_in_favorites| 11. Нельзя добавить повторно туже книгу в избранное                 | test_add_book_in_favorites_same_book                  |
|add_book_in_favorites | 12. Добавляет книгу в список избранного, если он не пуст            | test_add_book_in_favorites_and_list_not_empty         |
|add_book_in_favorites | 13. Нельзя добавить книгу не из books_genre                         | test_add_book_in_favorites_if_book_not_in_books_genre |
|delete_book_from_favorites | 14. Удаляет книгу из избранного                                     | test_delete_book_from_favorites                       |


**Запустить тесты из терминала можно такой командой:**

_pytest -v tests.py_