for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split()))for _ in range(100)]
    # 좌, 우 변화값
    l, r = [0, -1], [0, 1]
    ans = 0

    for i in range(100):
        if ladder[0][i]:
            cur = [1, i]

            while True:
                if cur[0] == 99:
                    break

                if cur[1] + l[1] >= 0 and ladder[cur[0] + l[0]][cur[1] + l[1]]:
                    while cur[1] + l[1] >= 0 and ladder[cur[0] + l[0]][cur[1] + l[1]]:
                        cur[0] += l[0]
                        cur[1] += l[1]
                    cur[0] += 1

                elif cur[1] + r[1] < 100 and ladder[cur[0] + r[0]][cur[1] + r[1]]:
                    while cur[1] + r[1] < 100 and ladder[cur[0] + r[0]][cur[1] + r[1]]:
                        cur[0] += r[0]
                        cur[1] += r[1]
                    cur[0] += 1

                else:
                    cur[0] += 1

            if ladder[cur[0]][cur[1]] == 2:
                ans = i
                break

    print("#{} {}".format(tc, ans))

'''
[Code Review]
- 나는 진짜 사다리 타는것 처럼 위에서 아래로 하나하나 다 찾아서 2의 위치로 가는 시작점을 찾는식으로 구현했는데 (그래도 통과..!)
- 생각해보니 사다리타기 답 구할때 맨 마지막점에서 당첨자를 찾고, 위로 올라가면서 어느위치에 답이 있는지 구할수있자나!!
- 그럼 반복문을 더 많이 돌 필요도 없음...!!!
- 거꾸로 돌리는 코드도 작성해봅시더..!
'''
