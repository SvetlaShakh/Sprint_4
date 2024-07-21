import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

# add_new_book
    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

    books_len_from_1_to_40 = ['А', 'Аб', 'Торт-Пирог Торт-Пирог Торт-Пирог Торт39',
                              'Торт-Пирог Торт-Пирог Торт-Пирог Торт 40']

    @pytest.mark.parametrize('book', books_len_from_1_to_40)
    def test_add_new_book_len_name_more_then_0_and_less_then_41_add_one_book(self, book):
        collector = BooksCollector()

        collector.add_new_book(book)

        assert len(collector.books_genre) == 1

    books_len_0_and_more_then_40 = ['', 'Торт-Пирог Торт-Пирог Торт-Пирог Пирог 41',
                                    'Торт-Пирог Торт-Пирог Торт-Пирог Пирог 042',
                                    'Торт-Пирог Торт-Пирог Торт-Пирог Торт-Пирог Торт-Пирог 57']

    @pytest.mark.parametrize('book', books_len_0_and_more_then_40)
    def test_add_new_book_len_name_0_and_more_then_40_add_zero_book(self, book):
        collector = BooksCollector()

        collector.add_new_book(book)

        assert len(collector.books_genre) == 0

    def test_add_new_book_same_name_add_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.books_genre) == 1

    def test_add_new_book_add_book_without_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

# set_book_genre
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_from_genre_set_genre(self, collector, genre):

        collector.set_book_genre('Гордость и предубеждение и зомби', genre)

        assert collector.books_genre['Гордость и предубеждение и зомби'] == genre

    def test_set_book_genre_not_from_genre_genre_isnt_genre(self, collector):

        collector.set_book_genre('Гордость и предубеждение и зомби', 'Абвгд')

        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    def test_set_book_genre_not_from_books_genre_is_none(self, collector):

        assert collector.set_book_genre('Henry Ford', 'Детективы') is None  # сообщение об ошибке/ ожидаемый результат

# get_book_genre
    def test_get_book_genre_get_set_genre(self, collector):

        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_book_is_not_books_genre_is_none(self, collector):

        assert collector.get_book_genre('Henry Ford') == None  # сообщение об ошибке/ ожидаемый результат

# get_books_with_specific_genre
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_get_lst_books_for_genre(self, collector_lst, genre):

        books_for_genre = []
        for name, book_genre in collector_lst.books_genre.items():
            if book_genre == genre:
                books_for_genre.append(name)

        assert collector_lst.get_books_with_specific_genre(genre) == books_for_genre

    def test_get_books_with_specific_genre_not_genre_in_lst_empty_list(self, collector_lst):

        assert collector_lst.get_books_with_specific_genre('Абвгд') == []  # сообщение об ошибке/ ожидаемый результат

# get_books_genre
    def test_get_books_genre_get_dict_all_books(self, collector_lst):

        assert collector_lst.get_books_genre() == collector_lst.books_genre

# get_books_for_children
    def test_get_books_for_children_get_list_books_without_age_rating(self, collector_lst):

        collector_lst.add_new_book('Книга без жанра')

        lst_books_for_children = []
        genre_age_rating = ['Ужасы', 'Детективы']
        lst_genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        for name, genre in collector_lst.books_genre.items():
            if genre not in genre_age_rating and genre in lst_genre:
                lst_books_for_children.append(name)

        assert collector_lst.get_books_for_children() == lst_books_for_children

# add_book_in_favorite
    def test_add_book_in_favorite_add_two_book(self, collector):

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.favorites) == 2

    def test_add_book_in_favorite_book_not_in_books_genre_add_zero_book(self, collector):

        collector.add_book_in_favorites('Henry Ford')

        assert len(collector.favorites) == 0

    def test_add_book_in_favorite_two_same_book_add_one_book(self, collector):

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.favorites) == 1

# delete_book_from_favorites
    def test_delete_book_from_favorites_zero_book_in_favorites(self, collector):

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites_book_not_in_lst_one_book_in_favorites(self, collector):

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Henry Ford')

        assert len(collector.favorites) == 1

#get_list_of_favorite_books
    def test_get_list_of_favorites_books_get_lst_name_of_favorites_books(self, collector):

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
