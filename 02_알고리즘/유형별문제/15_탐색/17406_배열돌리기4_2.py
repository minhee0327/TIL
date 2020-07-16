from copy import deepcopy

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
Q = [tuple(map(int, input().split())) for i in range(K)]

ans = 10000
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def value(arr):
    return min([sum(i) for i in arr])


def convert(arr, qry):
    r, c, s = qry
    r, c = r-1, c-1
    new_arr = deepcopy(arr)
    for i in range(1, s+1):
        sr, sc = r-i, c+i
        for w in range(4):
            for _ in range(i*2):
                nr, nc = sr+dx[w], sc + dy[w]
                new_arr[nr][nc] = arr[sr][sc]
                sr, sc = nr, nc
    return new_arr


def dfs(arr, qry, st):
    if st == (1 << K) - 1:
        return value(arr)
    ret = 50000
    for i in range(K):
        if st & 1 << i == 0:
            ret = min(ret, dfs(convert(arr, qry[i]), qry, st | 1 << i))
    return ret


print(dfs(A, Q, 0))
