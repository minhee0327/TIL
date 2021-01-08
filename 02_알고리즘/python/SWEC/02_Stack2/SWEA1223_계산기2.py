def priority(v):
    if v == '+':
        return 1
    elif v == '*':
        return 2


def posFix(lst, L):
    ret, stack = [], []

    while len(lst):

        value = lst.pop(0)

        if value not in '+-*/()':
            ret.append(eval(value))
        else:
            if len(stack) == 0:
                stack.append(value)
            elif priority(stack[-1]) < priority(value):
                stack.append(value)
            else:
                while True:
                    if len(stack) == 0 or priority(stack[-1]) < priority(value):
                        break
                    ret.append(stack.pop())
                stack.append(value)
    while len(stack):
        ret.append(stack.pop())

    return ret


def calc(a, b, i):
    if i == '+':
        return a+b
    elif i == '*':
        return a*b


def findValue(lst):
    stack = []
    while True:
        if len(lst) == 0:
            break
        i = lst.pop(0)
        if str(i) not in '+*':
            stack.append(i)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(calc(a, b, i))
    return stack[0]


for t in range(10):
    L = int(input())
    lst = list(input())

    # 후위연산으로 연산자 우선순위에 맞게 변형
    temp = posFix(lst, L)
    # 후위연산 결과를 계산결과 출력
    print("#{} {}".format(t+1, findValue(temp)))
