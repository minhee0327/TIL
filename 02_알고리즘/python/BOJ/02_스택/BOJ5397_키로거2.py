T = int(input())

for _ in range(T):
    string = input()
    left, right = [], []
    for s in string:
        if s == '-':
            if left:
                left.pop()
        elif s == '<':
            if left:
                right.append(left.pop())
        elif s == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(s)
    left.extend(reversed(right))
    print(''.join(left))


'''
* 추가사항
- from sys import stdin으로 속도를 줄일 수 있다.
- 입력받을 때, input() 대신 stdin.readline().strip() 이런 형태로 입력받는 연습하자.
'''
