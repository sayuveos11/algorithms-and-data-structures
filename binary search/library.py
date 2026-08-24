books = [
    "1984",
    "Dune",
    "Harry Potter",
    "It",
    "Metro 2033",
    "The Hobbit"
]

def book_search(books_list, item):
    low = 0
    high = len(books_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = books_list[mid]

        if guess == item:
            return f"Here is your book {guess}"

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return "This book is not available at the library"

print(book_search(books, 'It'))
