N, M = map(int, input().split())

listen = [input() for _ in range(N)]
speak = [input() for _ in range(M)]

listen = set(listen)
speak = set(speak)

ans = list(listen & speak)

print(len(ans))
for s in sorted(ans):
    print(s)
