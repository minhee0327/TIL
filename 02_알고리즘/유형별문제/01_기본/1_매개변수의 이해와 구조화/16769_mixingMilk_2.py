bucket, milk = [0, 0, 0], [0, 0, 0]

for i in range(3):
    bucket[i], milk[i] = map(int, input().split())

for i in range(100):
    now, nxt = i % 3, (i+1) % 3

    milk[now], milk[nxt] = max(
        0, milk[nxt] + milk[now] - bucket[nxt]), min(milk[nxt] + milk[now], bucket[nxt])

for m in milk:
    print(m)
