def findRow(arr):
    ans = 0
    for i in arr:
        ans = max(ans, sum(i))
    return ans


def findCol(arr):
    ans = 0
    for i in range(len(arr)):
        temp = 0
        for j in range(len(arr)):
            temp += arr[j][i]
        ans = max(ans, temp)
    return ans


def findDia(arr):
    # 동남쪽, 서남쪽
    es, ws = 0, 0
    for i in range(len(arr)):
        es += arr[i][i]
        ws += arr[i][-i]
    return max(es, ws)


for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    print("#{} {}".format(t, max(findRow(arr), findCol(arr), findDia(arr))))
