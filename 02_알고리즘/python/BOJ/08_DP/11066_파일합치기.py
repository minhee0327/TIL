def process():
    N = int(input())
    A = list(map(int, input().split()))
    # DP[i][j] : i에서 j까지 합하는데 필요한 최소비용


for _ in range(int(input())):
    process()


'''
크누스 알고리즘(Knuth Optimization)
- 특수한 조건에서, O(N³) => O(N²)까지 줄일 수 있는 알고리즘!

- C[i][j] : i부터 j까지의 비용
- D[i][j] : i부터 j까지의 최소 비용 캐싱

- 조건1: 사각부등식(quadrangle inequality)
    - C[a][c] + C[b][d] <= C[a][d] + C[b][c] (a<=b<=c<=d)
- 조건2: 단조성(monotonicity) 
    - C[b][c] <= C[a][d] (a<=b<=c<=d)
- 조건3: DP점화식
    - D[i][j] = min(DP[i][k]+ DP[k][j]) + C[i][j] (i<=k<=j)

- 조건 1,2 를 만족하면 조건3형태의 점화식을 사용해서 문제해결 가능.
'''
