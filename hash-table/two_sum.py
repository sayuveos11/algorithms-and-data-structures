numbers = [2, 7, 11, 15]
target = 9

def two_sum(numbers, target):
    seen = {}

    for i, num in enumerate(numbers):
        result = target - num

        if result in seen:
            return [seen[result], i]

        seen[num] = i

print(two_sum(numbers, target))