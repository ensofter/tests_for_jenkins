from ..good_function_most_common import most_common_word_on_web_page
from ..good_function_most_common import most_common_word
from pytest import raises


def test_with_mock():
    class TestResponse:
        text = 'aa bbb c'

    class TestUserAgent:
        def get(self, url):
            return TestResponse

    result = most_common_word_on_web_page(['a', 'b', 'c'], 'https://leadrock.com', user_agent=TestUserAgent())

    assert result == 'b', 'most common word'


def test_most_common_word():
    assert most_common_word(['a', 'b', 'c'], 'abbbcc') == 'b', 'most common in one string'


def test_most_common_word_empty_candidate():
    with raises(Exception, message='empty word raises'):
        most_common_word([], 'abc')


def test_most_common_ambiguous_result():
    assert most_common_word(['a', 'b', 'c'], 'ab') in ('a', 'b')
