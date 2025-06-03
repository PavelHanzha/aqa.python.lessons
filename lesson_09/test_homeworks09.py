import pytest
from lesson_09.homeworks import (
    sum_of_numbers_int,
    sum_of_numbers_float,
    delete_extra_space,
    count_symbols_in_text,
    the_longest_word_in_list
)


@pytest.mark.parametrize('input_equation, expected_result', [
    ('7,5,4,5,6', 27), # simple numbers
    ('4,-4,5', 5), # numbers with negative value
    ('0,0,4', 4), # list if numbers with "0"
    ('123gh', 'Не можу це зробити!') # invalid value
])

def test_sum_of_numbers_int(input_equation, expected_result):
    actual = sum_of_numbers_int(input_equation)

    assert actual == expected_result

@pytest.mark.parametrize('input_equation, expected_result', [
    ('5.5,4.5,2.7', 12.7), # all number with dot
    ('5,8,9,6', 28), # all number without dot
    ('-4.3,7.03,28', 30.73), # in list present number with negative value
    ('1.2,25.3,d,5', 'Не можу це зробити!'), # invalid value
])

def test_sum_of_numbers_float(input_equation, expected_result):
    actual = sum_of_numbers_float(input_equation)

    assert actual == expected_result


@pytest.mark.parametrize('input_text, expected_result', [
    ('   Hello  my friend    ', 'Hello my friend'), # extra space before/between/after words
    ('     Hello my friend', 'Hello my friend'), # extra space before words
    ('Hello my friend       ', 'Hello my friend'), # extra space after words
    ('Hello      my    friend', 'Hello my friend'), # extra space between words
    ('Hello my friend', 'Hello my friend'), # without extra space
])

def test_delete_extra_space(input_text, expected_result):
    actual = delete_extra_space(input_text)

    assert actual == expected_result

@pytest.mark.parametrize('input_text, expected_result', [
    ('qwertyuiop', 10), # only simple symbols in lower register
    ('QWERTYUIOP', 10), # only simple symbols in upper register
    ('!@#$%^&*()_', 11), # only special symbols
    ('1234567890987654321', 19), # only numbers
    ('123$%^qweRTY', 12), # special symbols, upper and lower symbols, numbers
])

def test_count_symbols_in_text(input_text, expected_result):
    actual = count_symbols_in_text(input_text)

    assert actual == expected_result



@pytest.mark.parametrize('input_text, expected_result', [
    (['Momo', 'and', 'Comon'], 'Comon'), # simple list with words
    (['Momo and Comon', 'Hello world!'], 'Momo and Comon'), # objects with several words
    (['', ''], ''), # empty list
    (['Jojo are the best', ''], 'Jojo are the best'), # list with empty last object
    (['', 'Jojo are the best'], 'Jojo are the best'), # list with empty 1st object
    (['123654', 'qwert'], '123654'), # list with numbers
    (['!@#$%$#@!', 'qwertyhgfd', '1234567876565421'], '1234567876565421'),
    # list with numbers/special and simple symbols
    (['One object in list'], 'One object in list') # One object in list
])

def test_the_longest_word_in_list(input_text, expected_result):
    actual = the_longest_word_in_list(input_text)

    assert actual == expected_result

