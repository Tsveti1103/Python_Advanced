n = int(input())
grades = {}
for _ in range(n):
    name, grades_as_str = input().split()
    grade = float(grades_as_str)
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for data in grades.items():
    print(f"{data[0]} -> {' '.join([f'{el:.2f}' for el in data[1]])} (avg: {(sum(data[1]) / len(data[1])):.2f})")
