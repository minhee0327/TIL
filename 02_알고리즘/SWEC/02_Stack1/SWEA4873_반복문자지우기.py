for t in range(1, 1+int(input())):
    string = input()
    stack = []

    for i in range(len(string)):
        if len(stack) == 0:
            stack.append(string[i])
        elif stack[-1] == string[i]:
            stack.pop()
        else:
            stack.append(string[i])

    print("#{} {}".format(t, len(stack)))

'''
[Code Review]
- 처음에는 2중반복문이 생각나서 계속 그렇게 접근했는데, 조건이 엄청나게 길어졌다.
- 그래서 BOJ의 키로거 문제를 떠올렸는데, stack에 담아두고, 다음에 오는값이 stack의 마지막 값과 일치하면 빼주는 방식을 선택했다.
'''
