array = input()

for i in range(9, -1, -1):
    for j in array:
        if int(j) == i:
            print(i, end="")


'''
1. 다른풀이
    - 자릿수를 기준으로 정렬하므로 9~0까지 차례로 확인
    - 각 숫자에 대하여 해당 숫자의 갯수를 계산하여 출력
'''
