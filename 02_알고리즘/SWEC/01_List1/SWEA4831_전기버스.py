for t in range(1, 1+int(input())):
    K, N, M = map(int, input().split())
    pos = [0] * (N+1)
    idx, cnt = 0, 0

    # 충전소 리스트에 해당하는 위치(pos)에 1로 가능여부 체크
    chungjeon = list(map(int, input().split()))
    for c in chungjeon:
        pos[c] += 1

    # 종점에 도달할때까지 반복
    while idx < N:
        ck = False
        # 종점의 위치보다 무사히 통과가능할 경우
        if idx + K >= N:
            break

        # 버스 이동중 갈수있는 최대거리부터, 최소거리까지 확인
        for i in range(idx+K, idx, -1):
            if pos[i]:
                idx = i
                cnt += 1
                ck = True
                break
        # 버스 이동으로 정류장 까지 못가게 되면, 불가능한경우니까, cnt를 0으로 하고 종료
        if ck == False:
            cnt = 0
            break

    print("#{} {}".format(t, cnt))
