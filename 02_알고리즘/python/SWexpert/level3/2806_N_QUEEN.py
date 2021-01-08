def n_queen(N, cur):
    global cnt

    if cur == N:
        cnt += 1
        return

    for i in range(N):
        isPossible = True
        for j in range(cur):
            if(arr[j] == i or i == arr[j] + (cur-j) or i == arr[j] - (cur-j)):
                isPossible = False
                break
        if(isPossible):
            arr[cur] = i
            n_queen(N, cur+1)


for t in range(1, 1+int(input())):
    N = int(input())
    arr = [0 for _ in range(N)]
    cnt = 0
    n_queen(N, 0)

    print("#{} {}".format(t, cnt))
