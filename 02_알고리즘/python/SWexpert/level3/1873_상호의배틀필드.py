# 방향벡터 사용문제
for t in range(1, 1+int(input())):
    # H, W Map의 높이 너비, N: 사용자가 입력한 문자열수, use: 사용자가 입력할 문자
    H, W = map(int, input().split())
    Map = [list(input())for _ in range(H)]
    N = int(input())
    use = input()

    state = [".", "*", "#", "-"]
    direction = ["^", "v", "<", ">"]
    string = ["U", "D", "L", "R", 'S']
    tank_dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # U, D, L, R에 따른 offset
    position = [0, 0, 0]  # 현재 위치 행, 렬, 방향idx값 저장.

    for i in range(H):
        for j in range(W):
            if Map[i][j] in direction:
                position[0] = i
                position[1] = j
                position[2] = direction.index(Map[i][j])
                Map[i][j] = '.'
    for u in use:
        user_idx = string.index(u)
        if user_idx < 4:
            i_idx = position[0] + tank_dir[user_idx][0]
            j_idx = position[1] + tank_dir[user_idx][1]
            if 0 <= i_idx < H and 0 <= j_idx < W:
                if Map[i_idx][j_idx] == '.':
                    position[0] = i_idx
                    position[1] = j_idx
            position[2] = user_idx

        else:
            # 현재 탱크 위치
            nx, ny = position[0], position[1]
            while True:
                nx, ny = nx + tank_dir[position[2]
                                       ][0], ny + tank_dir[position[2]][1]
                if 0 <= nx < H and 0 <= ny < W:
                    if Map[nx][ny] == '*':
                        Map[nx][ny] = '.'
                        break
                    elif Map[nx][ny] == '#':
                        break
                else:
                    break

    Map[position[0]][position[1]] = direction[position[2]]
    print('#{}'.format(t), end=" ")
    for m in Map:
        print("".join(m).format())

'''
[Code Review]
- 문제를 보고 많은 조건을 할 생각에 잠시 멍해졌던 문제...
- 이럴 경우에는 먼저 문제 입출력을 보면서 입출력 먼저 받아서 조금씩 해결해나가는 것도 괜찮은 방법이라고 생각한다.
- 방향벡터 문제가 어느정도 익숙해졌다고 생각했는데 조금 더 익숙해질 필요성을 느낀다..ㅠㅠ
'''
