def ICP(v):
    if v == '+':
        return 1
    elif v == '*':
        return 2
    elif v == '(':
        return 3


def ISP(v):
    if v == '+':
        return 1
    elif v == '*':
        return 2
    elif v == '(':
        return 0


def posFix(lst, L):
    ret, stack = [], []
    # ISP = {'+': 1, '*': 2, '(': 0}
    # ICP = {'+': 1, '*': 2, '(': 3}

    while len(lst):
        value = lst.pop(0)

        if value not in '+-*/()':
            ret.append(eval(value))

        elif value in ')':
            while True:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    ret.append(stack.pop())
        else:
            if len(stack) == 0:
                stack.append(value)
            elif ISP(stack[-1]) < ICP(value):
                stack.append(value)
            else:
                while True:
                    if len(stack) == 0 or ISP(stack[-1]) < ICP(value):
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

    temp = posFix(lst, L)

    print("#{} {}".format(t+1, findValue(temp)))

'''
[Code Review]
- 구현 순서
- posFix 함수에서 연산자와 피연산자에 따라 후위 표기법으로 변환하였다.
    - 연산하고자하는 문자열의 크기만큼 반복
        - 숫자일 경우, ret에 맞바로 담았고
        - 연산자일 경우 오른쪽 괄호일 경우와 아닐경우를 나누어 생각함
            - 오른쪽 괄호일 경우
                - '('를 만날 때까지 스택에서 뽑아, ret에 담아주었고
                - '('를 만나면 해당 괄호를 뽑고, 반복문 종료
            - 오른쪽 괄호가 아닐경우
                - 스택이 비어있으면 연산자를 넣어준다.
                - 비어있지 않을경우, 스택의 top의 우선순위와, 들어올 우선순위에 맞게 처리
                    - 만약 들어오고자 하는 연산자의 우선순위가 크면 스택에 넣어준다.
                    - 그게 아니라면 들어오고자하는 연산자의 우선순위가 스택의 top 값보다 클때지 반복해서 빼서 ret에 담아준다.
                        - (만약 스택이 비어있거나, 우선순위가 들어오고자하는게 커지면 반복문 종료)
    - 반목문 종료후에도 스택이 비어있으면, 스택내부 연산자들을 이어주고 ret반환
    - temp 에 할당

- findValue 함수에서 후위표기법으로 변환된 문자열을 계산했다.
    - 연산자가 아니면 그냥 stack에 담았고
    - 연산자에 해당하면 2개의 값을 빼내서, 먼저들어갔던 값에서 나중에 들어간값을 계산(calc)
    - 계산결과를 다시 stack에 담아주고 반복
    - 문자열만큼 순회를 하면 스택에 남은 결과값 return해주어 출력한다.
- 참고
    - ICP: 스택 외부에 있을때 우선순위
    - ISP: 스택 내부에 있을때 우선순위
    - 왼쪽 괄호의 우선순위가 내,외부에 따라 다르다. 내부에 있을때는 가장 낮고, 외부에 있을때는 가장 높다.
    - 처음에 나누기 빼기까지 구현했는데, 나누기 연산에서 소수의 처리를 어떻게 해야할지 조건에 따라 다를 것 같아서 제외했다.
    - ISP, ICP를 함수로 구현한것이 dict보다 살짝 빨라서 그대로 두었다. 
'''
