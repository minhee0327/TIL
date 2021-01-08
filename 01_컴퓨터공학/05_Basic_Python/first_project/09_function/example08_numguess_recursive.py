'''
1. 로직을 실행할 때 예외상황에서 재귀호출을 많이 사용.
'''
import random

# print(answer)
def numguess(try_cnt = 5, answer = random.randint(1,100)):
    while True:
        if try_cnt == 0:
            print("기회를 모두 소진하였습니다.\n 정답은 {} 였습니다.".format(answer))
            break
        n = input_answer()
        if n == answer:
            print("정답은 {} 였습니다.".format(answer))
            break
        elif n < answer:
            print("정답은 {}보다 큽니다.".format(n))
        else:
            print("정답은 {}보다 작습니다.".format(n))
        try_cnt -= 1

def input_answer():
    try:
        n = int(input("입력해주세요: "))
        return n
    except:
        return input_answer()

numguess()