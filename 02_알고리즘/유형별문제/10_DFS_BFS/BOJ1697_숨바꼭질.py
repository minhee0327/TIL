import sys

N, K = map(int, sys.stdin.readline().split())
count = [0] * 100001


def bfs(x):
    need_visit = []
    need_visit.append(x)

    while need_visit:
        x = need_visit.pop(0)
        dx = [x-1, x+1, x*2]

        if x == K:  # 방문하려는 값이 K값과 같으면
            return count[x]  # 해당 위치의 depth출력.
        for nx in dx:
            if nx < 0 or nx > 100000:
                continue
            elif not count[nx]:
                need_visit.append(nx)
                count[nx] = count[x] + 1  # (이전에 방문 안했을때만, 이전 depth 기준 +1)


print(bfs(N))
# print(count)

'''
[5]
[4,6,10]
[3, 5, 8, 5, 7, 12, 9, 11, 20]
이런식으로 반복

처음에는 count변수를 두고, counting을 했는데 그러다보니 반복문을 도는 카운트를 다 세서,
count 를 배열로 두고, depth를 계속 저장해나가는 방식으로 구현

'''
