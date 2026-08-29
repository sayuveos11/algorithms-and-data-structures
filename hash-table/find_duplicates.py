numbers = [4, 7, 2, 4, 9, 7, 1, 2, 5]

hash_dict = {}
result = []

for number in numbers:
    if number not in hash_dict:
        hash_dict[number] = 1
    else:
        hash_dict[number] += 1

for k, v in result.items():
    if v > 1:
        result.append(k)

print(result)