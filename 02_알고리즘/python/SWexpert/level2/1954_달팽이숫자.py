for t in range(1, 1+int(input())):
    N = int(input())
    x, y = 0, 0
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    B = [[0 for i in range(N)]for i in range(N)]

    cnt = 1

    for i in range(N-1, -1, -2):
        for w in range(4):
            for j in range(i):
                B[x][y] = cnt
                cnt += 1
                x, y = x + dx[w], y + dy[w]

            # 뱡향 바꾸기 위해 넣은 코드
            if w == 3 and x == y:
                x += 1
                y += 1

    # N이 짝수일 때 마지막 회전이 안돌아서 넣어줌.
    if N % 2 != 0:
        B[x-1][y-1] = cnt

    # 출력
    print("#{}".format(t))
    for b in B:
        for i in b:
            print(i, end=" ")
        print()

'''
[Code Review]
- 풀기는 혼자 풀어냈는데, 영 코드가 맘에 들지 않는다..
- 맞추려고 끼워넣은 기분이 물씬 들고..
- 어찌저찌 퍼즐맞추듯 맞춰서 풀리긴 했는데... 그래서 다른 사람 코드를 참조해서
- 조금씩 변형을 계속 해나갈까하는데, 2번이후로 계속 변형코드 올려야겠다.
'''
