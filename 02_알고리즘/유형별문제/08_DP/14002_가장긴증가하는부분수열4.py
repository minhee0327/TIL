N = int(input())
A = [0] + list(map(int, input().split()))

DP = [0] * (N+1)  # 길이정보
rev = [-1] * (N+1)  # 역추적할 정보(idx)

for i in range(1, N+1):
    for j in range(1, i, 1):
        if A[i] > A[i-j] and DP[i] < DP[i-j]:
            DP[i] = DP[i-j]
            rev[i] = i-j
    DP[i] += 1


print(max(DP))

ans = []
max_idx = DP.index(max(DP))

while max_idx != -1:
    ans.append(A[max_idx])
    max_idx = rev[max_idx]
ans.reverse()

print(' '.join(map(str, ans)))

'''
[CODE REVIEW]
https://br-brg.tistory.com/14
- 수열을 역추적하는 것은 처음 접했다...ㅠㅠ
- 처음 했을때, 계속 최대 길이는 구했는데, 그 경로를 출력하는것에 너무 애를 먹어서
- 좋은 방법을 찾아보니, 역추적이라는 개념을 보았다.
- 다시 반복해서 봐야할 듯한 문제!!ㅠㅠ
'''
