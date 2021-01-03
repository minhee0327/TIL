# sol1: 중첩 반복문을 사용해서 겨우 풀렸는데.. 뭔가 더 좋은 방법이 없을까...?
'''
A, B, C, N = map(int, input().split())

for i in range(300):
    for j in range(150):
        for k in range(100):
            if  A*i + B * j + C*k == N:
                print(1)
                exit()

print(0)
'''

# sol2: DP 활용
# DP는 A, B, C의 조합으로 idx값을 만들수 있다면 1을 아니면 0을 담는 배열
A, B, C, N = map(int, input().split())
DP = [0] * 301
DP[A] = DP[B] = DP[C] = 1

for i in range(A, N+1):
    for j in [A, B, C]:
        if i >= A and DP[i-j] == 1:
            DP[i] = 1

print(DP[N])
