def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]

        if guess == item:
            return guess

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

num_list = [1, 2, 3, 4, 5, 6]
print(binary_search(num_list, 5))