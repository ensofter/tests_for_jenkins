from ..binar_search import binar_search
from pytest import raises
from allure_commons._allure import step


def test_search_element():
    with step("-->Поиск элемента вконце"):
        assert binar_search(2, [1, 2, 3, 4]) == 1


def test_search_last_element():
    with step("-->Поиск элемента в середине"):
        assert binar_search(4, [1, 2, 3, 4]) == 3


def test_search_first_element():
    with step("-->Поиск элемента вначале"):
        assert binar_search(1, [1, 2, 3, 4]) == 0


def test_search_exception_not_found():
    with step("-->Проверяем исключение"):
        with raises(ValueError):
            binar_search(-1, [2, 3, 4, 5])

        with raises(ValueError):
            with step("-->Проверяем исключение"):
                binar_search(1, [2, 3, 4, 5])

        with raises(ValueError):
            with step("-->Проверяем исключение"):
                binar_search(5, [1, 2, 3, 4])

        with raises(ValueError):
            with step("-->Проверяем исключение"):
                binar_search(3, [1, 2, 4, 5])

