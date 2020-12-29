from queue import deque


def bfs(r, c, fr, fc):
    dx, dy = [1, 2, 2, 1, -1, -2, -2, -1], [-2, -1, 1, 2, 2, 1, -1, -2]
    q = deque()
    q.append([r, c])
    chess[r][c] = 1

    while q:
        # 현재 chess 위치
        cr, cc = q.popleft()
        # 현재 chess == 목적지 chess면 그동안 카운트 한 값 반환
        if cr == fr and cc == fc:
            return chess[fr][fc]-1

        for i in range(8):
            nx, ny = cr + dx[i], cc + dy[i]
            if 0 <= nx < I and 0 <= ny < I and chess[nx][ny] == 0:
                q.append([nx, ny])
                chess[nx][ny] = chess[cr][cc] + 1


T = int(input())

for _ in range(T):
    I = int(input())
    chess = [[0] * I for _ in range(I)]

    # 현재 r,c / 도달해야하는 r,c
    cur_r, cur_c = map(int, input().split())
    fin_r, fin_c = map(int, input().split())

    print(bfs(cur_r, cur_c, fin_r, fin_c))
