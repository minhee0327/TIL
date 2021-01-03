from copy import deepcopy

N = int(input())
Board = [list(map(int, input().split()))for i in range(N)]


def slide(lst, N):
    # i가 양수인 값만 new_list로 추출
    new_list = [i for i in lst if i]

    # 2 2 2 2 => 4 0 4 0 으로 바꾸기위한 과정
    for i in range(1, len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2
            new_list[i] = 0

    # 다시 0 제외하고, 양수만 남김.
    new_list = [i for i in new_list if i]
    return new_list + [0] * (N-len(new_list))


def rotate90(Board, N):
    NewBoard = deepcopy(Board)
    for i in range(N):
        for j in range(N):
            NewBoard[j][N-(i+1)] = Board[i][j]
    return NewBoard


def dfs(N, Board, count):
    ret = max([max(i)for i in Board])
    if count == 0:
        return ret

    # 상,하,좌,우 4가지
    for _ in range(4):
        X = [slide(x, N) for x in Board]
        if X != Board:
            ret = max(ret, dfs(N, X, count-1))
        Board = rotate90(Board, N)

    # print(Board)
    return ret


print(dfs(N, Board, 5))


'''
[Code Review]
- 상하좌우(4가지 case)를 5번 확인 => 최대 4**5(1024)의 경우
- 상하좌우 모두 따로 생각하면 너무 오랜 시간이 걸린다.

- 보통은, map을 돌리는 경우를 생각하는게 좋다. (0,90,180,270도)
- 방향을 하나로 설정하고, map을 계속 돌린다.
- 예를들어 slide(밀기)는 왼쪽으로만 진행하고, 계속 rotate를 하게되면, 
 상, 하, 좌, 우로 slide한 결과와 동일하다.
- 우리는 map을 출력하는 것이아니기 때문에, 방향은 고려하지 않아도 된다.
- 따라서 map을 돌려가면서 같은방향으로 slide 하면 원하는 결과를 얻을수있다.

- 계속BFS를 하면서 확인하다가, 다음 BFS가 동일하면, 재귀를 멈춘다.(동일한 결과 출력되니까)

- SW expert에서 풀었던, 배열돌리기 문제(90,180,270도 회전 출력)를 생각하면, rotate가 좀 더 편할거같다.
- 90도씩 돌리는것은 나중을 위해 암기해두는 것도 좋을 듯하다.
'''
