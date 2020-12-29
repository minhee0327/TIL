def bfs(need_visit):
    # cnt 의미: depth
    cnt = 1

    while need_visit:
        # 다음 방문 노드를 담을 임시 배열
        temp = []

        while need_visit:
            node = need_visit.pop(0)
            # 다음 노드들을 확인하면서
            for i in graph[node]:
                # 방문했으면 그냥 지나가기
                if visited[i]:
                    continue
                # 다음노드가 도착하고자하는 곳이면 반환하기(depth)
                if i == G:
                    return cnt

                # 아직 도달 못했으면 임시배열에 지나간 곳 담기 및, 지나간곳(visited) 체크(1)
                visited[i] = 1
                temp.append(i)

        # 다음 depth에서 도착지점을 못찾았으면 depth를 증가시켜주고, 방문해야할 노드는 temp로 업데이트
        cnt += 1
        need_visit = temp

    return 0


for t in range(1, 1 + int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for _ in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    S, G = map(int, input().split())

    ans = 0
    visited[S] = 1
    ans = bfs([S])

    print("#{} {}".format(t, ans))
