n = int(input())

students_and_grades = {}

for _ in range(n):
    data = input().split()
    if data[0] not in students_and_grades.keys():
        students_and_grades[data[0]] = []
    students_and_grades[data[0]].append(float(data[1]))

for data in students_and_grades.items():
    print(f'{data[0]} -> {" ".join([f"{el:.2f}" for el in data[1]])} (avg: {(sum(data[1]) / len(data[1])):.2f})')