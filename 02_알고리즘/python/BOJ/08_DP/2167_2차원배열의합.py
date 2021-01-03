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

- 쿼리가 10000개정도. 
- 90000개의 계산이 필요. 
- 따라서 부분합이라는 개념을 사용해서 속도를 줄여야한다.

- 예(1차원 배열의 누적합):
- 배열1: [0,1,2,3,4,5,6,7,8,9]
- 배열1의 누적합: [0,1,3,6,10,15,21,28,36,45]
- 만약, 6- 9까지의 합을 알고싶다 => 누적합(45 - 15) = 30
- DP[i] = i까지의 합이라고 했을때,
- i부터 j까지의 합 : DP[i] - DP[i-j]


'''
