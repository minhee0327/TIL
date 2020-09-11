from collections import deque

# 괄호의 짝이 맞는지 판별하는 함수


def isCouple(l, r):
    changeLR = {"(": ")", "{": "}", "[": "]"}
    if changeLR[l] == r:
        return True
    return False


for t in range(1, 1+10):
    N = int(input())
    munja = deque(input())
    stack = []
    ck = True

    while(len(munja)):
        cur = munja.popleft()
        if cur in '{([':
            stack.append(cur)
        elif cur in '})]':
            if len(stack) == 0:
                ck = False
                break
            elif isCouple(stack[-1], cur):
                stack.pop()
            else:
                ck = False
                break

    if len(stack) or (not ck):
        print("#{} {}".format(t, 0))
    else:
        print("#{} {}".format(t, 1))
