
# Variant for int numbers in list

list_with_number1 = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]


def sum_of_numbers_int(list_numbers):
    try:
        sum_numbers = [int(k) for k in list_numbers.split(",")]
        return sum(sum_numbers)
    except ValueError:
        return "Не можу це зробити!"


results_1 = [sum_of_numbers_int(item) for item in list_with_number1]

for result in results_1:
    print(result)

# Variant for numbers woth dot in list

list_with_number2 = ["1.1,2.2,3.3,4.4", "1.05,2.05,3.236,4.1,50", "qwerty1,2,3"]


def sum_of_numbers_float(list_numbers2):
    try:
        sum_numbers_float = sum(float(k) for k in list_numbers2.split(","))
        return sum_numbers_float
    except ValueError:
        return "Не можу це зробити!"


results_2 = [sum_of_numbers_float(item) for item in list_with_number2]

for result in results_2:
    print(result)

