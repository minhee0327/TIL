string = input()

temp, ans = '', ''
check = False

for i in string:
    if i == ' ':
        if check:
            ans += ' '
        else:
            ans += temp[::-1]+' '
            temp = ''
    elif i == '<':
        check = True
        ans += temp[::-1] + '<'
        temp = ''
    elif i == '>':
        ans += '>'
        check = False
    else:
        # check = False (괄호 밖에 있을 때)
        if not check:
            temp += i
        else:
            ans += i
ans += temp[::-1]
print(ans)

'''
1. 조건을 생각하는게 1시간이 넘어가서 stop하고 정해 풀이를 참조.
2. 큰 조건부터 세부조건으로 나누어가니까 이해 됬다.
3. 먼저 공란(' '), 부등호('<','>'), 일반 단어를 만나는 조건을 생각해본다.
4. 그 다음에 괄호 안에 있는지 유무를 파악할 ck 변수를 둔다.
5. 그래서 만약 3번 조건중에 괄호 내부에 있는지에 따라 swap을 해서 이어나갈지, 그냥 답을 이어나갈지 정한다.
    5-1. ck가 False면, 괄호 밖에 있으니까, temp를 역순으로 이어나감.
    5-2. ck가 True면, 괄호 내부에 있으니까, ans에 이어나가면 된다.
'''
