import pytest

from conftest import detective_books, horror_books, comedy_books, anime_books, fantasy_books, seven_sym, fourty_one_sym


class TestBooksCollector:

    # 1. проверяем, что добавилось именно две
    def test_add_new_book_add_two_diferent_books(self, collector):
        collector.add_new_book(horror_books)
        collector.add_new_book(fantasy_books)

        assert len(collector.get_books_genre()) == 2


    # 2 Добавление книги 40 символов в названии

    def test_add_new_book_with_namelen_more_40(self, collector):
        name = 'Странная история доктора Джекила и мистер'
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0


    # 3 Можно ли добавить 2 одинаковых книги
    def test_add_new_book_add_two_books_same_name(self, collector):
        collector.add_new_book(horror_books)
        collector.add_new_book(horror_books)

        assert len(collector.get_books_genre()) != 2


    # 4. Устанавливаем жанр книги
    def test_set_book_genre(self, collector, ready_books):
        assert collector.get_book_genre(horror_books) == 'Ужасы'


    # 5. Добавление книги в жанр по имени
    def test_get_books_genre_add_new_book_with_no_genre(self, collector):
        collector.add_new_book(horror_books)

        assert collector.get_book_genre(horror_books) == ''


    # 6. Выводим список книг с определённым жанром
    def test_get_books_with_specific_genre(self, collector, ready_books):
        book_genre = 'Ужасы'

        assert collector.get_books_with_specific_genre(book_genre) == [horror_books]


    # 7. Жанр книги не выводится, если его нет в books_genre
    def test_set_book_genre_no_genre_not_in_books_genre(self, collector, ready_books):
        book_genre = 'Мифы'

        assert collector.get_book_genre(book_genre) == None


    # 8. возвращаем книги, подходящие детям
    def test_get_books_for_children(self, collector, ready_books):

        assert collector.get_books_for_children() == [comedy_books, anime_books, fantasy_books]


    # 9. Книги с возрастным рейтингом отсутствуют в списке книг для детей

    @pytest.mark.parametrize('name, result',
                             [
                                 (detective_books, False),
                                 (horror_books, False),
                                 (comedy_books, True),
                                 (anime_books, True),
                                 (fantasy_books, True)
                                 ]
                             )
    def test_get_books_for_children_no_adult_genre(self, collector, ready_books, name, result):
        books_for_child = collector.get_books_for_children()
        assert (name in books_for_child) == result


    # 10. Добавляет книгу в избранное
    def test_add_book_in_favorites_and_list_is_empty(self, collector, ready_books):
        collector.add_book_in_favorites(horror_books)

        assert collector.get_list_of_favorites_books() == [horror_books]

    # 11. Нельзя добавить повторно туже книгу в избранное
    def test_add_book_in_favorites_same_book(self, collector, ready_books):
        collector.add_book_in_favorites(horror_books)
        collector.add_book_in_favorites(horror_books)

        assert len(collector.get_list_of_favorites_books()) != 2

    # 12. Добавляет книгу в список избранного, если он не пуст
    def test_add_book_in_favorites_and_list_not_empty(self, collector, ready_books):
        favority_list = ['Морковь в космосе', 'Космо Хилл']
        for favority in favority_list:
            collector.add_book_in_favorites(favority)
        collector.add_book_in_favorites(comedy_books)

        assert len(collector.get_list_of_favorites_books()) == 3

    # 13. Нельзя добавить книгу не из books_genre
    def test_add_book_in_favorites_if_book_not_in_books_genre(self, collector, ready_books):
        collector.add_book_in_favorites('Кот на крыше')

        assert len(collector.get_list_of_favorites_books()) != 1

    # 14. Удаляет книгу из избранного
    def test_delete_book_from_favorites(self, collector, ready_books):
        favority_list = ['Морковь в космосе', 'Космо Хилл']
        for favority in favority_list:
            collector.add_book_in_favorites(favority)

        assert len(collector.get_list_of_favorites_books()) == 2

