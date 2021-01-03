N, r, c = map(int, input().split())

# Z: 0,0을 기준으로 x,y의 숫자


def Z(sz, x, y):
    if sz == 1:
        return 0
    sz //= 2
    for i in range(2):
        for j in range(2):
            if x < sz * (i+1) and y < sz * (j+1):
                return (i*2+j) * sz*sz + Z(sz, x-sz*i, y-sz*j)


print(Z(2**N, r, c))

'''
1. sz//=2 : 변의 길이의 절반
2. (i*2+j) : 반복문을 돌면서 각각 1,2,3,4를 뜻함.
3. sz*sz: 해당 정사각형 갯수
4. 재귀적으로 작아지면서 r,c를 확인하고 그 위치에서 반환.

[참고]
1. 속도나 시간측면은 같고
2. 코드량이 대폭 감소. 
'''
