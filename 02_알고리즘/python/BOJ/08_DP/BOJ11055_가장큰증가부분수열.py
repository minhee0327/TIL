from copy import deepcopy

N = int(input())
A = list(map(int, input().split()))
DP = deepcopy(A)


for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j]+A[i])

print(max(DP))


'''
[Code Review]
- DP[i] =max(DP[i], DP[j]+A[i])
- 여기서 기존 DP[i] 값과 비교하는 과정을 넣지 않고, DP[j]+A[i]만 고려해서 틀렸었다.
- max로 비교하는 이유를 생각해보는데 오래걸렸다.

- 일단 예로 A가 {1 4 2 5} 인경우를 생각해보면 이유를 알기 좋았다.
- 1, 4, 5가 최대 크기 이기 때문에, 기존 값이 크기 때문에 DP[i] 값과 비교를 해야했다.
- 이렇게 예외를 처리하는게 생각보다 어려운 작업이라고 생각한다.(쉬워보이는 척해서 어렵다.)
- 다음부터는 실수 않길!
'''
