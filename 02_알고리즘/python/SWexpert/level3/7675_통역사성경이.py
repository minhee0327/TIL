for t in range(1, 1+int(input())):
    N = int(input())
    statement = input().split()
    ans = [0 for _ in range(N)]
    idx = 0

    for i in range(len(statement)):
        isNum = 1
        ck = 0

        for s in statement[i]:
            if s.isupper():
                ck += 1
            if s.isnumeric():
                isNum = 0
                break
        if ck and isNum:
            ans[idx] += 1
        if '.' in statement[i] or '!' in statement[i] or '?' in statement[i]:
            idx += 1

    print("#{}".format(t), end=" ")
    for i in ans:
        print(i, end=" ")
    print()


'''
import re


def checkNum(s):
    for i in s:
        if i.isdigit():
            return False
    return True


for t in range(1, 1+int(input())):
    N = int(input())
    statement = input()
    separate_statement = re.split('[.!?]', statement)
    separate_statement = separate_statement[:-1]
    ans = []
    for i in range(N):
        cnt = 0
        arr = separate_statement[i].split()

        for s in arr:
            if s[0].isupper():
                if (s[1:].islower()and checkNum(s[1:])) or len(s[i:]) == 0:
                    cnt += 1
        ans.append(cnt)
    print("#{} ".format(t), end="")
    for i in ans:
        print(i, end=" ")
    print()

# tc가 몇개 통과 안되서 다시 풀어봄(위)
'''
