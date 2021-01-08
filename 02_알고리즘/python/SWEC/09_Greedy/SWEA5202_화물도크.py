for t in range(1, 1+int(input())):
    trucks = []
    for n in range(int(input())):
        s, e = map(int, input().split())
        trucks.append((s, e))

    # 이게 키 포인트인듯;; 나는 계속 start순으로 정렬했는데, 일찍 끝나는 순으로 정렬
    trucks = sorted(trucks, key=lambda x: x[1])

    cnt = 0
    finish = 0

    # print(trucks)

    while trucks:
        start, end = trucks.pop(0)
        # 그래서 이전 작업시간(finish)랑 다음 작업의 시작시간을 비교해서 시작시간이 큰 경우에만 count
        if start >= finish:
            cnt += 1
            finish = end

    print("#{} {}".format(t, cnt))
