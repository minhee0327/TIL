'''
0. 개선된 numguess
1. 컴퓨터가 난수를 생성(범위1~100)
2. 사용자로부터 입력을 받는다.
3. 입력받은 숫자가 정답과 같은지 비교한다.
4. 문제를 맞출 수 있는 기회만큼 반복
5. 맞추면 정답, 틀리면 오답
5-1. 틀린 경우 힌트 제공
5-2. 사용자가 입력한 숫자가 정답보다 큰지, 작은지 알려준다.
6. 기회를 다했다면 종료
7. 정답 맞췄을 대도 종
'''

import random
answer = random.randint(1,100)
# print(answer)
try_cnt = 5

while True:
    if try_cnt ==0:
        print("기회를 모두 소진하였습니다.\n 정답은 {} 였습니다.".format(answer))
        break
    n = eval(input("입력해주세요: "))
    if n == answer:
        print("정답")
        break
    elif n<answer:
        print("정답은 {}보다 큽니다.".format(n))
    else:
        print("정답은 {}보다 작습니다.".format(n))
    try_cnt -=1