'''
플로이드-와샬 알고리즘 처음 봐서 참조해서 풀었음
참조링크: (https://it-garden.tistory.com/247)
'''
import sys
INF = sys.maxsize
n, m = map(int, input().split())
matrix = [[INF] * (n) for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

# 3중 for문으로 중간에 들렀다 갈때의 합이 이전에 간 거리보다 짧을때 update나가는 방향
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 0
            elif matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

ans = []
for i in matrix:
    ans.append(sum(i))


for i in range(n):
    if min(ans) == ans[i]:
        print(i+1)
        break
