# a: 1번 장대
# b: 2번 장대
# c: 3번 장대

move = []


def hanoi(n, a, b, c):
    if n == 1:
        move.append([a, c])
    else:
        hanoi(n-1, a, c, b)
        move.append([a, c])
        hanoi(n-1, b, a, c)


hanoi(int(input()), 1, 2, 3)
print(len(move))
print('\n'.join([' '.join(str(i) for i in row) for row in move]))

# 하노이의 탑 (n이 1, 2, 3, 4까지 케이스를 모두 생각해보면서 구현하기)
# n 이 1개일 경우 => a번 장대, c번장대로 이동하면 끝
# n 이 2개일 경우
# => a번 장대, b번장대로 이동 (재귀로 honoi(n-1, a, c, b))
# => a번 장대, c번장대로 이동 (현재 상태에서 a=>c,즉 move.append([a,c]))
# => b번 장대, c번장대로 이동 (재귀로 honoi(n-1, b, a , c ))

# 이거.. 혼자 구현하기 어려워서 참조 함 : 
# https://bit.ly/2TPEzEv
