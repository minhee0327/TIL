def heappush(val):
    heap[cnt] = val
    cur = cnt
    parent = cur//2

    while parent:
        if heap[parent] > heap[cur]:
            heap[parent], heap[cur] = heap[cur], heap[parent]
            cur = parent
            parent = cur//2
        else:
            break


for t in range(1, 1 + int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    heap = [0] * (N+1)

    cnt = 0

    for i in lst:
        cnt += 1
        heappush(i)

    N //= 2
    ans = 0
    while N:
        ans += heap[N]
        N //= 2

    # print(heap)

    print("#{} {}".format(t, ans))
