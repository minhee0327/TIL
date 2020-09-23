from collections import deque


# 0~3번째 순서로 +1, -1, *2, -10 연산수행
def calcOP(i, num):
    if i == 0:
        return num + 1
    elif i == 1:
        return num - 1
    elif i == 2:
        return num * 2
    elif i == 3:
        return num - 10

# queue에 [현재값, cnt]를 저장해가면서 bfs로 탐색


def bfs(n):
    Q = deque([])
    Q.append([n, 0])
    visited[n] = 1

    while Q:
        cur_num, cnt = Q.popleft()
        for i in range(4):
            nxt_num = calcOP(i, cur_num)
            # 다음 값이 찾는 값과 같으면 cnt 반환
            if nxt_num == M:
                return cnt + 1
            # 100만보다 작은 자연수면서, 방문 안한경우에 방문.
            if 0 < nxt_num <= 1000000 and not visited[nxt_num]:
                Q.append([nxt_num, cnt+1])
                visited[nxt_num] = 1


for t in range(1, 1+int(input())):
    N, M = map(int, input().split())
    visited = [0] * 1000001

    print("#{} {}".format(t, bfs(N)))
