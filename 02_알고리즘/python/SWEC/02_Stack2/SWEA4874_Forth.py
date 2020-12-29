def calc(a, b, cur):
    if cur == '+':
        return a+b
    elif cur == '-':
        return a-b
    elif cur == '*':
        return a*b
    elif cur == '/':
        return a//b


def forth(lst):
    stack = []

    while True:
        # print(stack, lst)
        cur = lst.pop(0)
        if cur not in '+-*/.':
            stack.append(int(cur))
        elif cur == '.':
            if len(stack) > 1:
                return 'error'
            return stack.pop()
        else:
            # 중간에 연산자가 추가될 일은 없을것같아서 or 이후 제거함.
            # if len(stack) < 2 or str(stack[-1]) in '+-*/.' or str(stack[-2]) in '+-*/.':
            if len(stack) < 2:
                return 'error'
            b = stack.pop()
            a = stack.pop()
            stack.append(calc(a, b, cur))


for t in range(1, 1+int(input())):
    arr = list(input().split())

    print("#{} {}".format(t, forth(arr)))
