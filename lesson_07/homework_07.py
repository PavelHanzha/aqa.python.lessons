# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def multiplier_two_number(a, b):
    return a + b


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_list_number(list_numbers):
    if not list_numbers:
        return 0
    return sum(list_numbers) / len(list_numbers)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def string_in_reverse_order(string):
    if not string:
        return "empty string"
    return string[::-1]

# check_string = "kjhgfdsaaaaaa"
# check_string_2 = ""
# print(string_in_reverse_order(check_string_2))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def the_longest_word_in_list(list_with_word):
    if not list_with_word:
        return "empty list"
    return max(list_with_word)


check_list = ['1', '12', '123']
print(the_longest_word_in_list(check_list))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# homework 6.1
def counter_symbols_in_text(text):
    if 10 < (len(set(text))):
        return True
    else:
        return False

# check_text_1 = 'hgnvhgnvhgnvhnghvg'
# check_text_2 = 'nhgjfmckdirutjghsysterw'
# check_text_3 = ''
#
# print(counter_symbols_in_text(check_text_1))
# print(counter_symbols_in_text(check_text_2))
# print(counter_symbols_in_text(check_text_3))
#
# homework 4.3
def delete_extra_space(text):
    if not text:
        return 'empty text'
    else:
        text.strip()
        text = text.split()
        text = ' '.join(text)
        return text


# some_text_for_chek = '''dfjkdjf  dfkdjfkjd      kdfdkfjskdf
# sfjkdsjfhasdf sfdhsdf      sdfadsjf    '''
# some_text_for_chek_2 = ''''''
# print(delete_extra_space(some_text_for_chek))
# print(delete_extra_space(some_text_for_chek_2))

# homework 4.10

def count_word_in_text(text):
    if not text:
        return 'empty text'
    else:
        text_list = text.split()
        return len(text_list)


# check_text_list_1 = '1 2 3 4 5 6 7 g f d c v g f d'
# check_text_list_2 = ''
# print(count_word_in_text(check_text_list_1))
# print(count_word_in_text(check_text_list_2))

# homework 6.2
def counter_symbols_in_text(text):
    counter = 0
    if text is not True:
        return 'empty text'
    else:
        for k in text:
            counter += 1
        return counter