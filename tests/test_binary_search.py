from ..binar_search import binar_search
from pytest import raises


def test_search_element():
    assert binar_search(2, [1, 2, 3, 4]) == 1


def test_search_last_element():
    assert binar_search(4, [1, 2, 3, 4]) == 3


def test_search_first_element():
    assert binar_search(1, [1, 2, 3, 4]) == 0


def test_search_exception_not_found():
    with raises(ValueError):
        binar_search(-1, [2, 3, 4, 5])

    with raises(ValueError):
        binar_search(1, [2, 3, 4, 5])

    with raises(ValueError):
        binar_search(5, [1, 2, 3, 4])

    with raises(ValueError):
        binar_search(3, [1, 2, 4, 5])

