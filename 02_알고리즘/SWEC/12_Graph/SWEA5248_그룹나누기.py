# 4.루트노드를 재귀적으로 찾아서 반환
def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])

# 3. union을 하는 과정에서, root노드를 찾기


def union(x, y):
    # 3-1. y의 부모노드를 x의 부모노드로 합침
    parent[find(y)] = find(x)


for t in range(1, 1+int(input())):
    N, M = map(int, input().split())
    votes = list(map(int, input().split()))
    # 1.부모노드 초기화
    parent = [i for i in range(N+1)]

    # 2. 투표한 것을 돌면서, union
    for i in range(M):
        union(votes[i*2], votes[i*2+1])

    # 5. 합쳐진 노드들을 돌면서, 부모값만 중복되지 않게 담아줌.
    ans = set()
    for i in parent:
        ans.add(find(i))

    # 6. 담을 때, 0을 빼줘야함 (1번부터 시작)
    print("#{} {}".format(t, len(ans)-1))


'''
BOJ 친구찾기 네트워크 문제와 유사한 문제
'''
