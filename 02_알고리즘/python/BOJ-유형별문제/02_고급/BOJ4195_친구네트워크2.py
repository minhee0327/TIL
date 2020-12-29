def find(node):
    if node == parent[node]:
        return node
    else:
        # 3. 재귀적으로 계속 루트노드를 찾아감
        parent[node] = find(parent[node])
        return parent[node]


def union(A, B):
    A = find(A)  # A에 연결된 루트노드를 찾아 다시 A에 할당
    B = find(B)  # B도 마찬가지, 각 루트노드가 다를때만 서로 연결하기 위해 찾음.

    # 4. 두 루트노드가 다를 경우에만
    if A != B:
        parent[B] = A  # B의 루트노드를 A로 업데이트
        rank[A] += rank[B]  # depth는 A를 B만큼 늘려야 함


for _ in range(int(input())):
    parent,  rank = {}, {}
    for i in range(int(input())):
        A, B = input().split()  # 친구A, 친구 B

        # 1. parent랑 rank(depth) 초기화
        if A not in parent:
            parent[A] = A
            rank[A] = 1
        if B not in parent:
            parent[B] = B
            rank[B] = 1

        # 2. 친구 A, B union하기 (각 루트노드가 다를때, 연결)
        union(A, B)

        # 5. 루트노드를 찾아 그 depth를 출력하면 원하는 결과
        print(rank[find(A)])
