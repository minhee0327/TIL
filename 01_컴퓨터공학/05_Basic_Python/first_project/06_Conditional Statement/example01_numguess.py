#컴퓨터가 특정한 난수(random)를 만들고, 사용자가 만들어진 난수를 맞추는 게임
'''
1. 컴퓨터가 난수를 생성한다.( 범위: 1~100 )
2. 사용자로부터 숫자를 입력받는다.
3. 입력받은 숫자가 난수와 같은지 비교한다.
4. 같다면 정답, 틀리면 오답
'''

import random
answer = random.randint(1,100)
#print(answer)

n = eval(input("입력해주세요: "))
if n == answer:
    print("정답")
else:
    print("오답")