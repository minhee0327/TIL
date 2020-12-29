for t in range(1, 1+int(input())):
    N, M, K = map(int, input().split())
    password = list(map(int, input().split()))
    idx = 0

    for _ in range(K):
        # print(password, idx, idx+M, len(password))
        if len(password) == idx+M:
            password[idx+M:idx+M] = [password[idx+M-1] + password[0]]
            idx = -1
        else:
            i = (idx+M) % len(password)
            password[i:i] = [password[i-1] + password[i]]
            idx += M
            if idx+M > len(password):
                idx %= (len(password)-1)

    password = password[::-1]
    if len(password) >= 10:
        password = password[:10]
    print("#{} {}".format(t, ' '.join(map(str, password))))
