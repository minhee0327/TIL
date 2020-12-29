for t in range(1, 1+int(input())):
    ans = 0
    for _ in range(int(input())):
        p, x = map(float, input().split())
        ans += p*x
    print('#{} %.6f'.format(t) % ans)
