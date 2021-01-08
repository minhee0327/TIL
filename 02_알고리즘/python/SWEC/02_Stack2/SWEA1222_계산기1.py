# 후위표기 계산문제이기는 한데.. 연산자가 +만 있으면 나머지 다 더하면되지않나...
# 계산기2,3에서는 후위표기로 구현하겠음.
for t in range(10):
    L = int(input())
    lst = list(map(int, input().split('+')))
    print("#{} {}".format(t+1, sum(lst)))
