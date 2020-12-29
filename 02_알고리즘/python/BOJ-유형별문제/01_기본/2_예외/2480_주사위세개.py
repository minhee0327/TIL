dice = sorted(map(int, input().split()))

if len(set(dice)) == 1:
    print(dice[0]*1000 + 10000)
elif len(set(dice)) == 2:
    print(dice[1]*100 + 1000)
else:
    print(dice[-1]*100)

'''
1. 강사님 코드랑 차이 없어서 별도 파일 더 추가 안함.
'''
