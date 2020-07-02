bucket = []
milk = []
cycle = 0

for _ in range(3):
    c, m = map(int, input().split())
    bucket.append(c)
    milk.append(m)

for i in range(100):
    now = i % 3
    nxt = (i+1) % 3

    milk[now], milk[nxt] = max(
        0, milk[nxt] + milk[now] - bucket[nxt]), min(milk[nxt] + milk[now], bucket[nxt])

for m in milk:
    print(m)
