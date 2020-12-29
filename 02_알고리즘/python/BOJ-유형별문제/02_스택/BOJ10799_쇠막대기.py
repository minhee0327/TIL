stack = input()

total, temp = 0, 0

for i in range(len(stack)):
    # print(i, temp, total)
    if stack[i] == '(':
        temp += 1
    elif stack[i] == ')':
        temp -= 1
        if stack[i-1] == '(':
            total += temp
        else:
            total += 1
print(total)

'''
- ( 일경우, temp를 증가
- ) 를 만난 경우중
    - (가 이전에 있었으면 ()이므로 레이저로 자름. (total에 잘린만큼 더해줌)
    - )가 이전에 있었으면 레이저가 아니므로, 파이프의 꽁다리임 TOTAL에 하나만 더해줌
    - 문자열 끝까지 반복
'''
