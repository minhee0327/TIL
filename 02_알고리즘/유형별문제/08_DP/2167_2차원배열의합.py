N, M = map(int, input().split())
B = [list(map(int, input().split())) for i in range(N)]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    ans = 0
    if i == x and j == y:
        ans = B[i-1][j-1]
    else:
        for r in range(i-1, x):
            for c in range(j-1, y):
                ans += B[r][c]
    print(ans)

'''
[Code Review]
- PyPy3로 겨우 통과인데, DP로 풀면 속도가 대폭 줄어들어서 다시 풀어봐야할것같다.
- 부분합이라는 개념이 자리잡혀야할듯.
'''
