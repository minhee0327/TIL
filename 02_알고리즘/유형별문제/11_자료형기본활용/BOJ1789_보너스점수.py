N = int(input())
OX = input()
bonus = 0
total = 0

for i, e in enumerate(OX):
    if e == 'X':
        bonus = 0
    elif e == 'O':
        total += (i+1) + bonus
        bonus += 1

print(total)
