
def func(idx, sum):
    global cnt
    if idx >= N:
        return
    if sum > K:
        return
    if sum+arr[idx] == K:
        cnt += 1

    func(idx+1, sum)
    func(idx+1, sum+arr[idx])


for t in range(1, 1+int(input())):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    func(0, 0)
    print("#{} {}".format(t, cnt))
