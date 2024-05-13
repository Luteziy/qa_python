import pytest

from main import BooksCollector


@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector

detective_books = 'Морковь в космосе'
horror_books = 'Гордость и предубеждение и зомби'
comedy_books = 'Собака и кот'
anime_books = 'Синий трактор'
fantasy_books = 'Космо Хилл'
seven_sym = 'Морковь'
fourty_one_sym = 'Странная история доктора Джекила и мистер'


@pytest.fixture(scope='function')
def ready_books(collector):
    books_genre = [ (detective_books, 'Детективы'),
                    (horror_books, 'Ужасы'),
                    (comedy_books, 'Комедии'),
                    (anime_books, 'Мультфильмы'),
                    (fantasy_books, 'Фантастика'),
                    (seven_sym, '7 символов'),
                    (fourty_one_sym, '47 док'),
                    ]
    for book, genre in books_genre:
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

