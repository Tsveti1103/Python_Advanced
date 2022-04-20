jobs = [int(el) for el in input().split(", ")]
index = int(input())
jobs_indexes = jobs.copy()
result = 0
while True:
    current_num = min(jobs)
    result += current_num
    current_index = jobs_indexes.index(current_num)
    jobs_indexes[current_index] = None
    if current_index == index:
        print(result)
        break
    jobs.remove(current_num)
