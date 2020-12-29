money = [500, 100, 50, 10, 5, 1]

give = 1000 - int(input())
count = 0

for i in range(len(money)):
    if give // money[i] > 0:
        count += give // money[i]
        give = give % money[i]

print(count)
# O(N)
