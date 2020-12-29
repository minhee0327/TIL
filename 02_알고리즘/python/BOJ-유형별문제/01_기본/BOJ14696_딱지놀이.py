N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))
    a, A = A[0], sorted(A[1:])
    B = list(map(int, input().split()))
    b, B = B[0], sorted(B[1:])
    ans = 'D'
    while True:
        if A == B:
            break
        if len(A) == 0:
            ans = 'B'
            break
        elif len(B) == 0:
            ans = 'A'
            break
        elif A[-1] == B[-1]:
            A.pop()
            B.pop()
            continue
        elif A[-1] > B[-1]:
            ans = 'A'
            break
        elif A[-1] < B[-1]:
            ans = 'B'
            break
    print(ans)
