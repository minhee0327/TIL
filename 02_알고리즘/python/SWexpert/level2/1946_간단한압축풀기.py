for t in range(1, 1+int(input())):
    lst = []
    temp = ''
    for n in range(int(input())):
        C, K = input().split()
        K = int(K)

        while K:
            temp += C
            if len(temp) == 10:
                lst.append(temp)
                temp = ''
            K -= 1

    if len(temp):
        lst.append(temp)

    print("#{}".format(t))
    for i in lst:
        print(i)

'''
[Code Review]
- 내가 생각한 방법은 문자열이 완성될때마다, 리스트에 담기로 한 방법.

- 10줄이 된 문자열은 lst에 담고, 임시로 10줄이 될때까지 사용한temp를 비워준다.
- 마지막 회전에서 남은 문자열이 있는지 (tmep 길이 있는지) 확인하고, 있으면 lst에 붙여준다.
'''
