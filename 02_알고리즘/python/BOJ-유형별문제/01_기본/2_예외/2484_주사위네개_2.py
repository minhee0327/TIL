def money():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1:
        return lst[0] * 5000 + 50000
    if len(set(lst)) == 2:
        if lst[1] == lst[2]:
            return lst[1] * 1000 + 10000
        else:
            return (lst[1] + lst[2]) * 500 + 2000

    for i in range(3):
        if lst[i] == lst[i+1]:
            return 1000 + lst[i] * 100
    return lst[-1] * 100


N = int(input())

print(max(money() for i in range(N)))

'''
1. 강사님은 함수로 구현.
2. 나는 계속 max 값을 업데이트 하는 형식으로 진행했는데,
    반환값을 모두 받아서 그 중 max 값으로 출력함.
'''
