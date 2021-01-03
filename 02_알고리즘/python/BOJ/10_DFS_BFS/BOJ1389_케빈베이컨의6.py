from queue import deque


def bfs(x):
    q = deque()
    q.append(x)
    visited = [-1 for _ in range(n+1)]
    visited[x] = 0

    # 이전 방문한 곳까지 저장하면서 다음 노드에 cnt 증가
    while q:
        x = q.popleft()
        for i in friends[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                q.append(i)

    # -1 이 아닌경우에 모두 cnt에 저장해서 return
    cnt = 0
    for i in range(1, n+1):
        if visited[i] != -1:
            cnt += visited[i]

    return cnt


n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]
res = []

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

# 1번부터 n번사람까지 케빈베이컨 수 구하기
for i in range(1, 1+n):
    res.append(bfs(i))

# res를 돌면서 최소 값이랑 일치하는 index중 작은 값이므로 앞에서부터 돌면서 답 출력.
for i in range(len(res)):
    if min(res) == res[i]:
        print(i+1)
        break
