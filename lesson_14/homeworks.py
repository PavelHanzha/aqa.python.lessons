def average_score_int(list_numbers):
    try:
        sum_numbers = [int(k) for k in list_numbers.split(",")]
        return sum(sum_numbers) / len(list_numbers)
    except ValueError:
        return "Не можу це зробити!"

