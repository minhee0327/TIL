def Findrow(a, b, m):
    ck = True
    for i in range(b, b+k):
        if m[a][i] == 0:
            ck = False
            break
    if b+k < n:
        if m[a][b+k] == 1:
            ck = False
    return ck


def Findcol(a, b, m):
    ck = True
    # 만약 찾아야하는 문자 길이만큼 돌면서 0이 있음 찾고자하는 문자 X
    for i in range(a, a+k):
        if m[i][b] == 0:
            ck = False
            break
    # 만약 찾고자하는 문자열보다 한칸 넘어간 값에 1이 있다면 그것도 찾고자하는 문자 X
    if a+k < n:
        if m[a+k][b] == 1:
            ck = False
    return ck


for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    m = [list(map(int, input().split())) for i in range(n)]

    count = 0

    for i in range(n):
        for j in range(n):
            # 0 이 있으면 통과
            if m[i][j] == 0:
                continue

            # 첫번째부터 시작하거나, 아니면 찾고자하는 값의 앞칸이 0값이면
            if i == 0 or m[i-1][j] == 0:
                # 범위를 넘지 않는 경우까지만 검사
                if i <= n-k:
                    if Findcol(i, j, m):
                        count += 1

            if j == 0 or m[i][j-1] == 0:
                if j <= n-k:
                    if Findrow(i, j, m):
                        count += 1

    print("#{} {}".format(t, count))
