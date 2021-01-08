score = sorted([(int(input()), i)for i in range(1, 9)], key=lambda x: -x[0])
score = score[:5]

total = 0
index = []

for s in score:
    total += s[0]
    index.append(s[1])
index = sorted(index)
print(total)
print(' '.join(map(str, index)))
