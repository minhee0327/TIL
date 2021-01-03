N, M = map(int, input().split())
B = [list(map(int, input().split())) for i in range(N)]
# DP[i][j] = (1,1) 부터 (i,j)까지의 부분합
DP = [[0 for i in range(M+1)] for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = (DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]) + B[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1])

'''
- 2차원 배열의 누적합
- DP[i][j] = (DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]) + B[i-1][j-1]
- 여기서 DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] 의 의미: row로 온 누적값 + col로 온 누적값 - 대각선 누적값
(대각선 누적값이 두번 더해졌기 때문에, 한번 제외해주어야함.)
- B[i-1][j-1]: 자기자신

- 출력할때
- 누적합중에서 x,y에서 i,j까지의 값을 빼주면 부분합 결과를 얻을 수있음.
DP[i-1][j-1]을 더하는 이유는 두번 빠지기 때문.
'''
