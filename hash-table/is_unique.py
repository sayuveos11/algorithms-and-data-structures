def is_unique(numbers):

    unique_dict = {}

    for number in numbers:
        if number not in unique_dict:
            unique_dict[number] = 1
        else:
            unique_dict[number] += 1

    for item in unique_dict.values():
        if item > 1:
            return False

    return True

print(is_unique([1, 2, 3, 4, 2]))