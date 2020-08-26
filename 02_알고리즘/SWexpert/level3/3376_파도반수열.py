'''
def func(n):
    if n <=0:
        return 0
    elif n<=3:
        return 1
    elif n ==4:
        return 2
    else:
        return func(n-1) + func(n-5)

arr = []

for t in range(1, 1 + int(input())):
    N = int(input())
    arr.append("#{} {}".format(t, func(N)))

print("\n".join(arr))    
'''

'''
[Code Review]
- 내가 찾은 점화식: f(n) = f(n-1) + f(n-5)
- 또다른 점화식: f(n) = f(n-2) + f(n-3)

- 문제는 재귀로 했을때, 시간 초과가 떴음.(위 코드)
- 그래서 DP형태로 변경해서 통과
'''

for t in range(1, 1 + int(input())):
    N = int(input())
    DP = [1 for _ in range(N+1)]
    DP[0] = 0

    for i in range(4, N+1):
        DP[i] = DP[i-1] + DP[i-5]

    print("#{} {}".format(t, DP[-1]))