import pytest
from homeworks import (
    sum_of_numbers_int,
    sum_of_numbers_float,
    delete_extra_space,
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
    ('   Hello  my fiend    ', 'Hello my fiend'), # extra space before/between/after words
    ('     Hello my fiend', 'Hello my fiend'), # extra space before words
    ('Hello my friend       ', 'Hello my fiend'), # extra space after words
    ('Hello      my    friend', 'Hello my fiend'), # extra space between words
    ('Hello my fiend', 'Hello my fiend'), # without extra space
])

def test_delete_extra_space(input_text, expected_result):
    actual = delete_extra_space(input_text)

    assert actual == expected_result
