'''
# 시간초과 : 시뮬레이션으로 개미가 직접 돌아다닌 것을 확인해서 시간내로 통과 못한거같다.

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
dx, dy = 1, 1

while t:
    if 0 < p < w and 0 < q < h:
        p += dx
        q += dy
    # 꼭지점에 부딫힌경우
    elif (p == 0 and q == 0) or (p == w and q == 0) or (p == 0 and q == h) or (p == w and q == h):
        dx *= -1
        dy *= -1
        p += dx
        q += dy
    # 북쪽에 부딫혔거나, 남쪽에 부딫힌경우
    elif q == 0 or q == h:
        dy *= -1
        p += dx
        q += dy
    # 동쪽 or 서쪽에 부딫힌 경우
    elif p == 0 or p == w:
        dx *= -1
        p += dx
        q += dy
    t -= 1

print(p, q)

'''
# 참조링크 : https://hanstemcell.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EA%B0%9C%EB%AF%B8?category=672485
# 좌표의 규칙성을 찾았다면, 개미가 움직인 모든 거리를 체크 하지 않고도 풀 수 있었던 문제;; 윽...

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x_dir, y_dir = (p+t) // w, (q+t) // h

# (x, 좌우 좌표만 보는 경우)
# 짝수인 경우, 방향이 0 => w 로 가고있는중이므로
if x_dir % 2 == 0:
    p = 0 + (p+t) % w
# 훌수인 경우, 방향이 w => 0으로 가고있는중
elif x_dir % 2:
    p = w - (p+t) % w

# (y, 상하 좌표만 보는 경우)
if y_dir % 2 == 0:
    q = 0 + (q+t) % h
elif y_dir % 2:
    q = h - (q+t) % h

print(p, q)

'''
- 해설의 요지는
- x, y 좌표를 분리해서 생각하기

- 개미가 움직이는 x좌표만 봤을 때, 움직이는 방향에 따라 거리를 구할 수 있음
- 만약 0 => w로 가는 (오른쪽)중일경우에 (p+t) //w 의 값이 짝수일 경우임
- 이때 좌표 위치는 0으로 부터 시작해서 나머지만큼 간 위치이므로 0 + (p+t) %w
- 반대로 w => 0으로 가능중 (왼쪽)일 경우에 (p+t) //w 의 값이 홀수일 경우임
- 이때 좌표 위치는 w로부터 시작해서 나머지만큼 제외한 위치에 있으므로 w - (p+t) % w
- 이렇게하면 x 좌표를 구할 수 있음

- y좌표도 마찬가지로 0 => h/ h=> 0 으로 가는 방향에 따라 해당 좌표를 알 수 있다. 
'''
