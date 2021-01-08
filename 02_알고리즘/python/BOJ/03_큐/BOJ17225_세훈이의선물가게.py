A, B, N = map(int, input().split())
sangmin, jisu = [], []

for _ in range(N):
    t, c, m = input().split()
    t, m = int(t), int(m)+1
    while m:
        if c == 'B':
            if len(sangmin) == 0 or t > sangmin[-1]:
                sangmin.append(t)
            elif t <= sangmin[-1]:
                sangmin.append(sangmin[-1] + A)
            else:
                sangmin.append(sangmin[-1] + A)
        elif c == 'R':
            if len(jisu) == 0:
                jisu.append(t)
            elif t > jisu[-1]:
                jisu.append(t)
            elif t <= jisu[-1]:
                jisu.append(jisu[-1]+B)
            else:
                jisu.append(jisu[-1] + B)
        m -= 1

print(sangmin, jisu)
