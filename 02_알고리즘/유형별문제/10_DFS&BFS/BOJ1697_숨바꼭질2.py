from collections import deque
N, K = map(int, input().split())
count = [0] * 100001


def bfs(x):
    need_visit = deque([x])
    while need_visit:
        x = need_visit.popleft()
        dx = [x-1, x+1, x*2]
        if x == K:
            return count[x]
        for nx in dx:
            if nx < 0 or nx > 100000:
                continue
            elif not count[nx]:
                need_visit.append(nx)
                count[nx] = count[x] + 1  # (이전에 방문 안했을때만, 이전 depth 기준 +1)


print(bfs(N))
# print(count)

'''
1. dequeue를 사용했더니 속도가 반 넘게 줄었다..!
2. 속도 관련
    - list의 경우 pop(0) 의 경우 => O(N)
    - dequeue 의 경우 양방향으로 pop가능. => O(1)
3. pop(0)을 많이 해야하는 경우 dequeue자료구조 활용
4. sys.stdin.readline()속도 줄이기는 입력을 많이 받아야하는 경우에 사용하자.(입력 량 적으면 큰 차이 없음)
'''
