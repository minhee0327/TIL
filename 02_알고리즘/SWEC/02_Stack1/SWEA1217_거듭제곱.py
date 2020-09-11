def custom_pow(N, M):
    if N == 0 or M == 0:
        return 1

    if M % 2 == 0:
        return custom_pow(N, M//2) * custom_pow(N, M//2)
    else:
        return custom_pow(N, (M-1)//2) * custom_pow(N, (M-1)//2) * N


for _ in range(1, 1+10):
    t = int(input())
    N, M = map(int, input().split())

    print("#{} {}".format(t, custom_pow(N, M)))

'''
- 분할정복 예시를 보여주기위해 다시 구현함
- 예전에 구현했던게 속도는 더 빠르게 나옴..!

def fibo(n, m, ans):
    if m == 0:
        return ans
    else:
        ans *= n
        return fibo(n, m-1, ans)
 
 
for _ in range(10):
    t = int(input())
    n, m = map(int, input().split())
 
    print("#{} {}".format(t, fibo(n, m, 1)))
'''
