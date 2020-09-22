def dfs(nxt_idx):
    global ans, cnt

    # 마지막 정류소 도달했을 때, cnt값이 ans보다 작은 값이었다면 값교체
    if nxt_idx >= N-1:
        if ans > cnt:
            ans = cnt
        return

    # 결과가 중간에 계산중인값보다 작은경우에는 계산 필요 없음
    if ans < cnt:
        return

    # 탐색 (뒤에서부터 가능한 위치 찾아감)
    for i in range(nxt_idx + chargingStation[nxt_idx], nxt_idx, -1):
        cnt += 1
        dfs(i)
        cnt -= 1


for t in range(1, 1 + int(input())):
    temp = list(map(int, input().split()))

    N = temp[0]
    chargingStation = temp[1:]
    ans = 100
    cnt = 0
    dfs(0)

    # 첫번째 방문한 정료소는 제외하고 출력
    print("#{} {}".format(t, ans-1))
