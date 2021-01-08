def changeRight(s):
    if s == '[':
        return ']'
    if s == '{':
        return '}'
    if s == '(':
        return ')'


for t in range(1, 1+int(input())):
    #temp역할 : stack
    temp = []
    ck = 1

    for i in input():
        # 왼쪽괄호일경우, 오른쪽괄호로 빠꾸어서 스택에 담고
        if i in '{([':
            temp.append(changeRight(i))
        # 오른쪽 괄호일경우 스택이 비었거나, 스택의 마지막값과 일치하지 않으면 종료
        if i in '})]':
            if len(temp) == 0 or temp[-1] != i:
                ck = 0
                break
            elif temp[-1] == i:
                temp.pop()

    if len(temp) == 0 and ck:
        print("#{} {}".format(t, 1))
    else:
        print("#{} {}".format(t, 0))
