def dfs(cur):
    visited[cur] = 1
    # print(visited)
    if cur == 99:
        return
    if len(graph[cur]) == 0:
        return

    for node in graph[cur]:
        if visited[node] == 0:
            dfs(node)


for _ in range(10):
    t, n = map(int, input().split())
    pos = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visited = [0]*100

    for i in range(0, n*2, 2):
        graph[pos[i]].append(pos[i+1])

    # print(graph)

    dfs(0)
    if visited[-1]:
        print("#{} {}".format(t, 1))
    else:
        print("#{} {}".format(t, 0))

'''
통과는 했는데.. 이렇게 풀어도 되나 싶으다;;ㅎㅎ
일단 문제에서 몇번 회전하는지, 혹은 tc로 주어지는지가 안나와서 swea에서는 대부분 10번 돌아서 10번만 돌렸음.

- 입력받은 노드의 상태가 단방향이라서 append를 한방향으로만 했음

- 마지막 노드 99에 도달했을때는 더 진행할 필요 없으니가는 return해줌
- 혹시라도 갈 길이 없을경우(len(graph[cur])이 0)에도 못가도록 return해줌.
- 만약에 갈길이 있으면 반복해서 재귀적으로 그 다음 노드를 순회해보도록함. 

- 그래서 dfs를 돌면서 방문한 위치는 체크했고, 마지막 99번을 방문했을경우에는 1을 출력하고 아닐경우에는 0을 출력함.
'''
