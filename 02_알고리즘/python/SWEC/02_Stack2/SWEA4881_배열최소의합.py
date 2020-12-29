# r: 다음 행, ret: 현재 행까지의 합.
def func(r, ret):
    global ans
    # print(r, ret, visited)

    # 4. 마지막 행에 도달했을경우 ans가 가능한 최소값을 업뎃해준다.
    if r >= N:
        ans = min(ans, ret)
        return

    # 3. 다음행을 계속확인하는 절차
    # 3-1. ret> ans 인경우는 굳이 확인할 필요 없음. 그 전에 다녀온 곳이 더 작으니까.
    # 3-2. visited[i] = 0인경우는 그전 행들에서 방문하지 않은 열이니까 방문처리해주고 재귀적으로확인.
    # 3-3. 재귀를 돌고난 후, visited[i] = 0 해주어서 그 전 행의 위치 상태를 복귀시킴.!!! <= 이거 자주 못썼는데 첨 잘썼음!!
    for i in range(N):
        if ret > ans:
            continue
        if visited[i] == 0:
            visited[i] = 1
            func(r+1, ret+arr[r][i])
            visited[i] = 0

    return


for t in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    # ans가 가능한 최대 값
    ans = N * 9

    # 1. 맨 첫 행의 모든 열은 돌아봐야한다.
    for i in range(N):
        # 2. visited 배열은 방문했던 '열'을 체크하는 배열이다.
        visited = [0] * N
        visited[i] = 1
        func(1, arr[0][i])

    print("#{} {}".format(t, ans))

'''
[Code Review]
- 개인적으로는 토너먼트보다 금방 풀렸던 문제.
- 순서를 나중에라도 혹시 잊을까봐 순서대로 숫자부여해서 주석 설명 달아두었다..!
'''
