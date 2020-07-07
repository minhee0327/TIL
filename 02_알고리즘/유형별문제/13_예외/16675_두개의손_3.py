
ml, mr, tl, tr = ('RSP'.index(i) for i in input().split())

if ml == mr and (ml+2) % 3 in [tl, tr]:
    print("TK")
elif tl == tr and (tl+2) % 3 in [ml, mr]:
    print("MS")
else:
    print('?')

'''
같은 값을 냈을 때,

RSP의 경우 2칸 뛴 경우
SRP의 경우 1칸 뛴 경우가 동일할 때, 상대가 이긴다.
'''
