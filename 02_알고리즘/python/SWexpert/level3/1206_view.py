for t in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))
    ans = 0

    for i in range(2, len(building)-2):
        if building[i] > max(building[i-2], building[i-1], building[i+1], building[i+2]):
            ans += building[i] - max(building[i-2],
                                     building[i-1], building[i+1], building[i+2])

    print("#{} {}".format(t, ans))


'''
- 빌딩이 위치한 구간별로 좌2, 우2개의 값 총 4개의 값중 최댓값과, 현재 가리키고있는 빌딩의 차이가 양수면,
- 그 양수값을 ans에 더해서 최종 출력
- 검사하고자 하는 구간을 설정하는게 조금 시간이 걸렸음.
'''
