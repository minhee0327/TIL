# 원점으로부터  시계방향으로 돌아간 거리
def getDistance(x, y):
    # 북
    if x == 1:
        return y
    # 남
    elif x == 2:
        return r + c + r - y
    # 서
    elif x == 3:
        return r + c + r + c - y
    # 동
    elif x == 4:
        return r + y


r, c = map(int, input().split())
n = int(input())
total_len = (r+c) * 2
distanceFromZero = []   # 원점으로부터 거리를 계산해서 담은 배열
ans = 0                 # 답에는 최소 거리만 담는다(시계방향/반시계방향 둘중 최소)

for _ in range(n+1):
    x, y = map(int, input().split())
    distanceFromZero.append(getDistance(x, y))

dongen = distanceFromZero.pop()

for i in range(n):
    ans += min(abs(distanceFromZero[i] - dongen),
               total_len - abs(distanceFromZero[i] - dongen))

print(ans)
