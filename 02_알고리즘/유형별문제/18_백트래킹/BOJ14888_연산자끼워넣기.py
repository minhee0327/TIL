from itertools import permutations


def changeOP(lst):
    ret = []
    ret += lst[0] * ['+']
    ret += lst[1] * ['-']
    ret += lst[2] * ['*']
    ret += lst[3] * ['/']
    return ret


N = int(input())
A = list(map(int, input().split()))
op_num = list(map(int, input().split()))
op_arr = changeOP(op_num)

possibiliyt_op = list(permutations(op_arr, N-1))

min_v, max_v = 1000000000, -1000000000

for p in possibiliyt_op:
    stack = A[::-1]
    for i in p:
        a = stack.pop()
        b = stack.pop()
        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(a-b)
        elif i == '*':
            stack.append(a*b)
        elif i == '/':
            if a < 0 and b > 0:
                a *= -1
                stack.append((a//b) * -1)
            else:
                stack.append(a//b)

    if min_v > stack[0]:
        min_v = stack[0]
    if max_v < stack[0]:
        max_v = stack[0]

print(max_v)
print(min_v)

'''
- 시간초과로 다시 풀어보기!
'''
