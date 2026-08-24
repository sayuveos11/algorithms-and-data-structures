students = [
    ("Alex", 85),
    ("John", 92),
    ("Maria", 78),
    ("David", 95),
    ("Kate", 88)
]

def student_sort(students):
    for i in range(len(students)):
        min_index = i

        for j in range(i + 1, len(students)):
            if students[j][1] < students[min_index][1]:
                min_index = j

        students[i], students[min_index] = students[min_index], students[i]

    return students

print(student_sort(students))