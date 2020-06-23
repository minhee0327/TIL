import heapq

N, M = map(int, input().split())
where = list(map(int, input().split()))

positive, negative = [], []
largest = max(max(where), -min(where))

for w in where:
    if w > 0:
        heapq.heappush(positive, -w)
    else:
        heapq.heappush(negative, w)

result = 0

while positive:
    result += heapq.heappop(positive)
    for _ in range(M-1):
        if positive:
            heapq.heappop(positive)

while negative:
    result += heapq.heappop(negative)
    for _ in range(M-1):
        if negative:
            heapq.heappop(negative)

print(-result*2 - largest)


'''
어떻게 작은값을 빼낼까 고민하면서 sort를 생각했는데,
우선순위큐 최소힙을 생각하면 좋았을 것을 내가 구현하려다가 시간만 더 오래걸렸다...

작은 값부터 먼저 꺼낸다 혹은 큰값먼저 꺼낸다의 경우, 우선순위큐를 떠올리자.
'''
