list_with_number = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]


def sum_of_numbers(list_numbers):
    try:
        sum_numbers = [int(x) for x in list_numbers.split(",")]
        return sum(sum_numbers)
    except ValueError:
        return "Не можу це зробити!"


results = [sum_of_numbers(item) for item in list_with_number]

for result in results:
    print(result)
