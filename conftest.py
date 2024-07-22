import pytest

from main import BooksCollector
@pytest.fixture
def collector():
    collector = BooksCollector()

    collector.add_new_book('Гордость и предубеждение и зомби')

    return collector

@pytest.fixture
def collector_lst(collector):

    collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
    collector.add_new_book('Гордость и предубеждение и зомби V2')
    collector.set_book_genre('Гордость и предубеждение и зомби V2', 'Ужасы')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
    collector.add_new_book('Что делать, если ваш кот V2')
    collector.set_book_genre('Что делать, если ваш кот V2', 'Комедии')
    collector.add_new_book('38 попугаев')
    collector.set_book_genre('38 попугаев', 'Мультфильмы')
    collector.add_new_book('38 попугаев V2')
    collector.set_book_genre('38 попугаев V2', 'Мультфильмы')
    collector.add_new_book('Шерлок Холмс')
    collector.set_book_genre('Шерлок Холмс', 'Детективы')
    collector.add_new_book('Шерлок Холмс V2')
    collector.set_book_genre('Шерлок Холмс V2', 'Детективы')
    collector.add_new_book('351 градус по фарингейту')
    collector.set_book_genre('351 градус по фарингейту', 'Фантастика')
    collector.add_new_book('351 градус по фарингейту V2')
    collector.set_book_genre('351 градус по фарингейту V2', 'Фантастика')

    return collector
