numbers = [3, 8, 5, 10, 7, 2, 9]

def sum_even(numbers, index):
    if index < 0:
        return 0

    return (numbers[index] if numbers[index] % 2 == 0 else 0) + sum_even(numbers, index - 1)

print(sum_even(numbers, len(numbers) - 1))
