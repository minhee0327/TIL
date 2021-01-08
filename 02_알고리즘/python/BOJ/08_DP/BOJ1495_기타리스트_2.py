N, S, M = map(int, input().split())
V = list(map(int, input().split()))

DP = [[0]*(M+1) for _ in range(N+1)]
DP[0][S] = 1

for i in range(1, N+1):
    for j in range(M+1):
        if DP[i-1][j] == 0:
            continue
        if j - V[i-1] >= 0:
            DP[i][j-V[i-1]] = 1
        if j + V[i-1] <= M:
            DP[i][j+V[i-1]] = 1

result = -1
for i in range(M, -1, -1):
    if DP[N][i] == 1:
        result = i
        break

print(result)

'''
[결과]
- 통과
- 29416 KB = (29.416MB)
- DP에 결과값을 저장해가는 방법도 있지만, true/false(1/0)으로 저장해서
- 해당 인덱스를 출력하는 방법도 있다는 점을 기억하면 더 많은 문제를 해결 할 수 있을 것 같다.

- 또 출력할 때에도, 처음에는 M만큼 모두 돌면서 최대 값을 찾으려고 생각했는데
- 최대 값을 출력하니까 뒤에서 부터 돌면서 true인 값이 있을 경우 결과를 저장하고
- for문 스텝을 종료 하는것 또한 시간단축에 좋은 코드였다.
- (강사님 코드 참조해서 혼자 해석하고 혼자 다시 풀어본건데 역시 아직 갈길이 멀다.)
'''
