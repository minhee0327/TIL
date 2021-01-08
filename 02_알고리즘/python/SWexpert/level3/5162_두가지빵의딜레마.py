for t in range(1, 1+int(input())):
    A, B, C = map(int, input().split())
    ans = 0

    # A가 B보다 클 경우 SWAP
    if A > B:
        A, B = B, A

    # 가진돈(C)에서 A개 산만큼 증가
    ans += C // A
    C %= A

    # 거스름돈이 남아있으면, 또 증가시켜주기.
    if C >= B:
        ans += C//B
        C %= B

    print("#{} {}".format(t, ans))
