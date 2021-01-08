N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

S = 0
for i in range(N):
    S += (A[i] * B[N-i-1])

print(S)
