from collections import deque


# use bfs
def findEnd(r, c):
    visited[r][c] = 1
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    need_visit = deque([])
    need_visit.append([r, c])

    while(need_visit):
        r, c = need_visit.popleft()
        visited[r][c] = 1
        for i in range(4):
            nx, ny = dx[i] + r, dy[i] + c
            # 벽을 넘어섰거나, 이미 다녀왔던 곳은 더이상 진행 필요 없음.
            if nx < 0 or ny < 0 or nx >= 100 or ny >= 100 or miro[nx][ny] == '1' or visited[nx][ny]:
                continue
            # 0 일 경우엔 진행가능
            if miro[nx][ny] == '0':
                need_visit.append([nx, ny])
            # 3 일 경우엔 end point이므로 1반환(종료)
            if miro[nx][ny] == '3':
                return 1

    # 다 돌아봤는데 3을 못찾은 경우 0
    return 0


for _ in range(10):
    t = int(input())
    miro = [list(input()) for t in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    ans = 0
    # s: start position(row,col)
    s = [0, 0]

    # find start point
    for i in range(100):
        if '2' in miro[i]:
            s = [i, miro[i].index('2')]

    # find end point
    ans = findEnd(s[0], s[1])

    print("#{} {}".format(t, ans))

'''
1. 앞서 문제와 달리 반복문으로 해결해보았다.
2. 코테도 그렇고 항상 재귀로하면 뭔가 조건이 부족한건지 재귀 깊이에 걸렸었는데.. 이번에도 또 걸렸다.
3. 그래서 while문으로 방문할 필요성이 있는 곳과, 이미 다녀온 곳을 모두 체크해가면서 구현을 진행해 보았다.
4. 나는 은근 재귀를 할때 중간에 사고를 놓치는 경향이 있는데, 시간이 제한된 코테에서는 while문으로 구현하는 걸 떠올리는것도 
일종의 전략이라고생각한다.
5. 앞으로 재귀는 조금더 훈련해가야 할 필요가 있다..!
'''
