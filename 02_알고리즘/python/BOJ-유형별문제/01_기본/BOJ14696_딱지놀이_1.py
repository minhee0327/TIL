N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))
    a, A = A[0], sorted(A[1:])
    B = list(map(int, input().split()))
    b, B = B[0], sorted(B[1:])

    ans = ''
    for i in range(4, 0, -1):
        if A == B:
            ans = 'D'
            break
        elif A.count(i) == B.count(i):
            continue
        elif A.count(i) > B.count(i):
            ans = 'A'
            break
        elif A.count(i) < B.count(i):
            ans = 'B'
            break
    print(ans)
