n, l, k = map(int, input().split())

task = []
checked = [0] * n
count = 0
total = 0

for _ in range(n):
    sub1, sub2 = map(int, input().split())
    task.append((sub1, sub2))


for i in range(n):
    if task[i][1] <= l and checked[i] == 0 and count < k:
        total += 140
        count += 1
        checked[i] = 1

for i in range(n):
    if task[i][0] <= l and checked[i] == 0 and count < k:
        total += 100
        checked[i] = 1
        count += 1

print(total)
