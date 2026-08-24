input_num = int(input("Enter your number from 1 to 100: "))

def guess_number(low, high, target):
    if target < 1 or target > 100:
        raise ValueError("You need to enter a number between 1 and 100")

    while low <= high:
        mid = (low + high) // 2
        print(f"Computer guess: {mid}")

        if mid == target:
            return f"You guessed right! My number was {mid}"

        if mid > target:
            high = mid - 1
        else:
            low = mid + 1

    return None

print(guess_number(1, 100, input_num))