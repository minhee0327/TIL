people = sorted(int(input()) for _ in range(9))
total = sum(people)
ck = 0

for i in range(8):
    for j in range(i+1, 9):
        if total - (people[i] + people[j]) == 100:
            del people[j]
            del people[i]
            ck = 1
            break
    if ck:
        break

for p in people:
    print(p)
