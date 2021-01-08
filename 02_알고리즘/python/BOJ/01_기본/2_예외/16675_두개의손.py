lst = list(input().split())

for i in range(len(lst)):
    if lst[i] == 'S':
        lst[i] = 0
    elif lst[i] == 'R':
        lst[i] = 1
    elif lst[i] == 'P':
        lst[i] = 2

ml, mr, tl, tr = lst[0], lst[1], lst[2], lst[3]

if ml == mr and (ml+1) % 3 in [tl, tr]:
    print("TK")
elif tl == tr and (tl+1) % 3 in [ml, mr]:
    print("MS")
else:
    print("?")

'''
1. R, S, P 순으로 0, 1, 2 로 두고 풀었는데, 계속 뭔가 잘못된거같아
강사님 코드 기반으로 수정함.
2. S, R, P 순으로 두는 것만 수정했는데 조건 충족이 되었음
3. R, S, P 순으로 혹시 몰라서 한번 더 구현해봄(두개의 손 _3 참조)
'''
