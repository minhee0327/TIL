# 모듈러 형식으로 0 < 1, 1 < 2, 2 < 0
# 가위, 바위, 보를 숫자(index)로 표현
# find 내장함수를 사용하는 것도 좋다.

# S: 0, R: 1, P: 2
ml, mr, tl, tr = ('SRP'.index(i) for i in input().split())
#print(ml, mr, tl, tr)

# 태경이가 이기려면 민성이가 낸 것보다 1을 더한 값을 가지고 있을 때 이긴다
if ml == mr and (ml+1) % 3 in [tl, tr]:
    print("TK")
# 민성이가 이기려면 태경이가 낸것보다 1을 더한값을 가지고 있을때 이긴다
elif tl == tr and (tl+1) % 3 in [ml, mr]:
    print("MS")
else:
    print('?')
