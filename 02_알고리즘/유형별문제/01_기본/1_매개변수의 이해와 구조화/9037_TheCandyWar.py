for _ in range(int(input())):
    # N: 아이의 인원 ,  C: 초기 사탕 갯수
    N, C = int(input()), list(map(int, input().split()))
    # 순환수: count
    count = 0
    # 초기 candy 짝수로 setting
    for i in range(N):
        if C[i] % 2 != 0:
            C[i] += 1

    while len(set(C)) != 1:
        temp = [0] * N
        for i in range(N):
            temp[i] = C[i]//2
        for i in range(N):
            C[i] = temp[i-1] + temp[i]
            if C[i] % 2 != 0:
                C[i] += 1
        count += 1

    print(count)
