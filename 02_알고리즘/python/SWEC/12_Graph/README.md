# 그래프

-   ## 개요
    -   객체(사물 또는 추상적 개념) 들과 객체 사이의 연결관계
    -   N개의 정점을 가지는 그래프는 최대 N\*(N-1)/2 개의 간선가능 (무방향)
    -   그래프 표현
        -   인접 행렬(2차원배열로 간선 정보 저장)
        -   인접 리스트: 각 정점별로 인접 정점으로 나가는 간선의 정보를 저장한다.
-   ## 그래프 순회

    -   비선형 구조인 그래프로 표현된 모든 자료(정점) 빠짐없이 선택
    -   대표: DFS, BFS
    -   ### DFS
        -   stack
        -   재귀
            ```py
            # G: 그래프, v: 시작정점
            # visited: 정점의 방문정보 표시(False,초기화)
            # G[v]: 그래프G에서 v의 인접정점 리스트
            def DFS_recursive(G, v):
                visited[v] = True
                visit(v)
                for w in G[v]:
                    if not in visited:
                        DFS_recursive(G, w)
            ```
        -   반복
            ```py
            # G: 그래프,S:stack v: 시작정점
            # visited: 정점의 방문정보 표시(False,초기화)
            # G[v]: 그래프G에서 v의 인접정점 리스트
            def DFS_Iterative(G, v):
                S = [v]
                while S:
                    v = S.pop()
                    if v not in visited:
                        visited.append(v)
                        visit()
                        S.extend(G[v] - set(visited))
                    return
            ```
    -   ### BFS

        -   queue, priorityqueue, ...
        -   반목
            ```py
            # G: 그래프,Q:queue v: 시작정점
            # visited: 정점의 방문정보 표시(False,초기화)
            # G[v]: 그래프G에서 v의 인접정점 리스트
            def BFS(Q, v):
                Q.append(v)
                visited[v] = True
                while Q:
                    v = Q.pop(0)
                    if v not in visited:
                        visited.append(v)
                        Q.extend(G[v])
            ```
        -   BFS 확장

            ```py
            # D: 최단거리, P: 최단경로
            def BFS(Q,v):
                D[v] = 0
                P[v] = v
                Q.append(v)
                visited[v] = True

                while Q:
                    v = Q.pop(0)
                    for w in G[v]:
                        if not visited[w]:
                            Q.append(w)
                            visited[w] = True
                            D[w] = D[v] +1
                            P[w] = v
            ```

-   ## 상호배타집합
    -   서로소 또는 상호 배타 집합
        -   서로 중복 포함된 원소가 없는 집합들로 교집합이 없음
        -   집합에 속한 하나의 특정 원소(대표자)를 통해 각 집합들을 구분
        -   상호 배타 집합 표현방법
            -   연결리스트
            -   트리
        -   상호배타 집합 연산
            -   make-set(x): 원소 x만으로 구성된 집합 생성
            -   find-set(x): 임의의 원소 x가 속한 집합을 알아내기 위해 사용, 집합의 대표자를 알기 위한 연산
            -   union(x, y): x 원소가 속한 집합과 y원소가 속한 집합을 하나의 집합으로 합치는 연산
        -
