from copy import deepcopy

# 배열 A의 크기: NXM, 회전연산 갯수: K
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
# (r,c,s)
Q = [tuple(map(int, input().split())) for i in range(K)]

# 최대값: 50*100 => 약 10000으로 진행
ans = 10000
# dx, dy: 오른쪽 위 기준, 남=>서=>북=>동 방향
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

# 최소값


def value(arr):
    return min([sum(i) for i in arr])

# 중심점을 두고, 회전(방향 벡터로 진행)


def convert(arr, qry):
    # print(qry)/
    r, c, s = qry
    # r, c는 중심점인데, 배열의 시작이 0부터니까, 1씩 빼주어 중심 수정
    r, c = r-1, c-1
    new_arr = deepcopy(arr)

    # 회전을 할 건데, s만큼 회전은 반복함.
    for i in range(1, s+1):
        # 출발점
        sr, sc = r-i, c+i
        # 4번의 방향(오,아,왼,위)
        for w in range(4):
            # (동심원이 커질때마다, 2,4,6...씩커짐)
            for _ in range(i*2):
                nr, nc = sr+dx[w], sc + dy[w]
                new_arr[nr][nc] = arr[sr][sc]
                sr, sc = nr, nc
    return new_arr


# (r,c,s)에 다른 dfs 처리
def dfs(arr, qry):
    global ans
    # 쿼리 처리 끝난경우
    if sum(qry) == K:
        ans = min(ans, value(arr))
        return
    for i in range(K):
        if qry[i]:
            continue
        new_arr = convert(arr, Q[i])
        qry[i] = 1
        dfs(new_arr, qry)
        qry[i] = 0


dfs(A, [0 for i in range(K)])
print(ans)

'''
[Code Review]
- 1<=K<=6, K개 만큼 회전을 할 수있는데, 순서 상관 없음. 따라서 6!의 경우의수가 나옴.
- 비트마스크 기법
    - 비트를 통해 알 수 있는 2가지 정보
        - 이진수는 0,1만 가지고, true/false 상태를 가진다.
        - 이진수는 십진수로 표현이 가능하다.
    - 예 (출처: https://mygumi.tistory.com/361 [마이구미의 HelloWorld])
        { 0, 1, 2, 3, 4 } => 11111 => (2^4 * 1) + (2^3 * 1) + (2^2 * 1) + (2^1 * 1) + (2^0 * 1) = 31
        { 1, 2, 3, 4 } => 11110 => (2^4 * 1) + (2^3 * 1) + (2^2 * 1) + (2^1 * 1) = 30 
        { 1, 2, 4 } => 10110 => (2^4 * 1) + (2^2 * 1) + (2^1 * 1) = 22
        { 2, 4 } => 10100 => (2^4 * 1) + (2^2 * 1) = 20
        { 1 } => 00010 => (2^1 * 1) = 2
- 먼저 리스트로 만들어보고, 다음에 비트마스크로 작성.
'''
