products = [
    "Apple",
    "Banana",
    "Book",
    "Computer",
    "Keyboard",
    "Mouse",
    "Phone"
]

selected_product = input("What product are you looking for? ").capitalize()

def products_search(products_list, product):
    low = 0
    high = len(products_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = products_list[mid]

        if guess == product:
            return f"The item has been found. Index: {mid}"

        if guess > product:
            high = mid - 1
        else:
            low = mid + 1

    return "The item was not found."

print(products_search(products, selected_product))

