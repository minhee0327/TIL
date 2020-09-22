def recursive(idx, ans, add, sub, mul, div):
    global mx, mn

    if idx == N:
        mx = max(mx, ans)
        mn = min(mn, ans)
        return

    if add:
        recursive(idx+1, ans + A[idx], add-1, sub, mul, div)
    if sub:
        recursive(idx+1, ans - A[idx], add, sub-1, mul, div)
    if mul:
        recursive(idx+1, ans * A[idx], add, sub, mul-1, div)
    if div:
        if ans > 0:
            recursive(idx+1, ans // A[idx], add, sub, mul, div-1)
        else:
            recursive(idx+1, -1 * ((ans*-1) // A[idx]), add, sub, mul, div-1)


N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
mx, mn = -1000000000, 1000000000

recursive(1, A[0], op[0], op[1], op[2], op[3])
print("{}\n{}".format(mx, mn))
'''
- 위코드는 찾아서 보고 따라한 코드.
- 일단 재귀적으로 완전 탐색 접근을 못했었는데, 재귀적으로 탐색을 해나가는 것을 배웠다.
'''


'''
# 시간초과로 다시 풀어보기!
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
