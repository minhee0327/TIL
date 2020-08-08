import math

for t in range(1, 1+int(input())):
    N, A, B = map(int, input().split())

    min_v = 10000000000

    for i in range(1, N//2):
        R = i
        C = math.floor(N/i)

        if (R*C <= N):
            min_v = min(A*abs(R-C) + B*(N-R*C), min_v)

    R, C = int(math.sqrt(N)), int(math.sqrt(N))
    min_v = min(A*abs(R-C) + B*(N-R*C), min_v)

    print("#{} {}".format(t, min_v))
