n = int(input())

temp = []
pm = []
count = 1
possibility = True

for _ in range(n):
    num = int(input())
    while count <= num:
        temp.append(count)
        pm.append('+')
        count += 1
    if temp[-1] == num:
        temp.pop()
        pm.append('-')
    else:
        possibility = False


# print(pm)
if possibility == False:
    print('NO')
else:
    for i in pm:
        print(i)

# 내가 생각 못한 부분
# 1. possibilty (가능성) 체크
# 2. count 를 두고 증가시켜가면서 계산하는것 (첨에 배열로 1~n까지 두고 계산해서 오차 있었음..)
# 1번을 해결하지 않아서 런타임에러가 계속 났었음..! 다음에는 가능성 여부까지 고려 해서 설계합시다.
# 스택에서 원소를 연달아 빼낼 때 내림차순을 유지할 수 있는지 확인하자!
