def sum_of_numbers_int(list_numbers):
    try:
        sum_numbers = [int(k) for k in list_numbers.split(",")]
        return sum(sum_numbers)
    except ValueError:
        return "Не можу це зробити!"

def sum_of_numbers_float(list_numbers2):
    try:
        sum_numbers_float = sum(float(k) for k in list_numbers2.split(","))
        return sum_numbers_float
    except ValueError:
        return "Не можу це зробити!"

def delete_extra_space(text):
    if not text:
        return 'empty text'
    else:
        text.strip()
        text = text.split()
        text = ' '.join(text)
        return text

def count_symbols_in_text(text):
    if not text:
        return 'empty text'
    else:
        return len(text)

def the_longest_word_in_list(list_with_word):
    if not list_with_word:
        return "empty list"
    return max(list_with_word, key=len)

print(sum_of_numbers_int('7,5,4,5,6'))