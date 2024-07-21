import pytest

from main import BooksCollector
@pytest.fixture
def collector():
    collector = BooksCollector()

    collector.add_new_book('Гордость и предубеждение и зомби')

    return collector

@pytest.fixture
def collector_lst():
    collector_lst= BooksCollector()

    collector_lst.add_new_book('Гордость и предубеждение и зомби')
    collector_lst.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
    collector_lst.add_new_book('Гордость и предубеждение и зомби V2')
    collector_lst.set_book_genre('Гордость и предубеждение и зомби V2', 'Ужасы')
    collector_lst.add_new_book('Что делать, если ваш кот хочет вас убить')
    collector_lst.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
    collector_lst.add_new_book('Что делать, если ваш кот V2')
    collector_lst.set_book_genre('Что делать, если ваш кот V2', 'Комедии')
    collector_lst.add_new_book('38 попугаев')
    collector_lst.set_book_genre('38 попугаев', 'Мультфильмы')
    collector_lst.add_new_book('38 попугаев V2')
    collector_lst.set_book_genre('38 попугаев V2', 'Мультфильмы')
    collector_lst.add_new_book('Шерлок Холмс')
    collector_lst.set_book_genre('Шерлок Холмс', 'Детективы')
    collector_lst.add_new_book('Шерлок Холмс V2')
    collector_lst.set_book_genre('Шерлок Холмс V2', 'Детективы')
    collector_lst.add_new_book('351 градус по фарингейту')
    collector_lst.set_book_genre('351 градус по фарингейту', 'Фантастика')
    collector_lst.add_new_book('351 градус по фарингейту V2')
    collector_lst.set_book_genre('351 градус по фарингейту V2', 'Фантастика')

    return collector_lst
