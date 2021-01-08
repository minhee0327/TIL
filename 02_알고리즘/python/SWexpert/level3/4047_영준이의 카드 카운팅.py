for t in range(1, 1+int(input())):
    CARD = ['S','D','H','C']
    CARD_NUM = [[i for i in range(1, 14)] for _ in range(4)]

    #영준이가 가진 카드
    TXY = input()
    ck = 1

    for i in range(len(TXY)//3):
        # c: 영준이가 가진 카드 모양
        c = TXY[i*3]
        # num: 영준이가 가진 카드 넘버
        num = int(TXY[i*3+1: (i+1)*3])
        
        if num in CARD_NUM[CARD.index(c)]:
            CARD_NUM[CARD.index(c)].remove(num)
        else:
            ck = 0
            break
    
    if ck:
        print("#{}".format(t), end=" ")
        for i in CARD_NUM:
            print(len(i), end=" ")
        print()
    else:
        print("#{} {}".format(t, 'ERROR'))


'''
- 내가 푼 코드가 평상시보다 길어진거같아서 다른 분 풀이를 보니까
- 사고를 반대로 하는것이 좋겠다고 생각을 했다.
- 나의 경우에는 52장의 카드에서, 영준이가 가진 카드를 제외시켜가는 방향으로 생각했는데,

- 다른 분은 반대로 영준이가 가진 카드만 모아서, 겹치는지 유무를 set 자료형으로 확인한후, 겹치는 경우에는 error를, 
- 안겹치는 경우의 수만큼만 13장의 카드에서 각각 빼주면서 결과값을 도출하는 방향이 훨씬 코드도 간결하고 python스러웠다.
- (dict, set을 사용한 코드) 다음에 풀때는 시간이 허락된다면, 좀더 파이썬스러운 방향을 생각해보는것도 좋겠다. 
- 참고한 자료: https://mungto.tistory.com/159
'''