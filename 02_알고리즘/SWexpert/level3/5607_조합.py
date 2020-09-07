'''
# 통과가 안된다..뭔가 다른 방법이 필요하다.

for t in range(1, 1+int(input())):
    N, R = map(int, input().split())
    up, down = 1, 1

    for _ in range(R):
        up *= N
        N -= 1
        down *= R
        R -= 1

    print("#{} {}".format(t, int((up/down) % 1234567891)))
'''
