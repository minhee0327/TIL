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
시간초과....뭔가 다시 풀어보기
'''
