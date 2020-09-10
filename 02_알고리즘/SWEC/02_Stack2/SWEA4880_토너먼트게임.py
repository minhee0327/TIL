# a,b중 a가 가위바위보를 이겼는지 구현한 함수
def isFrontWin(a, b):
    # 앞에 애가 승 or 비김 = > true
    if (a+2) % 3 == (b % 3) or a == b:
        return True
    return False

# 앞, 뒤 절반씩 쪼개주는작업
# 만약 배열의 크기가 1개이하면, 해당 값을 리턴해주고
# 그 해당값의 idx가 1인 값은 가위,바위, 보니까 isFrontWin에 보내서
# 앞에애가 이겼다면 앞에애를 내보내주고, 뒤에애가 이겼으면 뒤에 애를 내보내준다.


def tournament(p):
    # print(p)
    if len(p) < 2:
        return p[0]

    front = p[:(len(p)-1)//2+1]
    back = p[(len(p)-1)//2+1:]

    f = tournament(front)
    b = tournament(back)

    if isFrontWin(f[1], b[1]):
        return f
    else:
        return b


for t in range(1, 1+int(input())):
    N = int(input())
    people = list(map(int, input().split()))

    for i in range(N):
        people[i] = (i+1, people[i])

    res = tournament(people)

    print("#{} {}".format(t, res[0]))

'''
- 생각보다 문제를 푸는데 오래 걸린문제
- 분할정복에 대한 생각을 했더라면 좀 더 빨랐을텐데 한참 돌아왔다..

- 그리고 중앙값에 대한 처리를 계속 잘못해서 홀짝에 따라 구분지어봤다가, 계산 계속 잘못해서 계속 틀림....
- front = p[:(len(p)-1)//2+1] 처럼 길이 하나를 빼고, 절반을 빼준다음 한개 증가시켜서
- 만약 사람수가 7명이였다면, 4명 3명 이렇게 나눌수있다......(이것때문에 계속 계산이 엇나가서 한참걸림...)
- 괄호 처리 잘하자..
'''
