for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split()))for _ in range(100)]

    # 당첨위치 바로 위칸을 현재 시작점(cur)으로 잡는다.
    cur = [98, ladder[99].index(2)]

    while True:
        # 사다리 맨 위에까지 돌았으면 멈춤
        if cur[0] == 0:
            break

        # 좌측으로 갈 경로가 있는경우
        if cur[1] - 1 >= 0 and ladder[cur[0]][cur[1]-1]:
            while cur[1] - 1 >= 0 and ladder[cur[0]][cur[1]-1]:
                cur[1] -= 1

        # 우측으로 갈 경로가 있는경우
        elif cur[1] + 1 < 100 and ladder[cur[0]][cur[1]+1]:
            while cur[1] + 1 < 100 and ladder[cur[0]][cur[1]+1]:
                cur[1] += 1

        # 좌, 우측 경로가 없으면 위로 올라감
        cur[0] -= 1

    print("#{} {}".format(tc, cur[1]))

'''
[Code Review]
- 코드 양은 줄었는데, 속도는 정말 미미한 차이.
- 속도차이가 나는 원인은.. 아무래도 배열안에 숫자로 받아서 그런가..
'''
