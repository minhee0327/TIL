def paperCount(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paperCount(n-1) + paperCount(n-2) * 2


for t in range(1, 1+int(input())):
    print("#{} {}".format(t, paperCount(int(input())//10)))


'''
[code review]
- 아...........
- 점화식을 못찾아서 한시간 내내 뻘뻘댄 문제..
- 왜못찾았냐하면 N=4인경우를 한땀한땀 그렸는데 뭔가 빼먹고 그리는바람에 계속 규칙이 안보였다.
- DP(n) = DP(n-1) + DP(n-2) * 2 (N>=3)
- 각 경우에 값을 하나라도 잘못 구하면 규칙을 찾는데 당연히 고생한다.... 꼼꼼하게 계산하자.
- 참고
    - N = 1 / Result = 1
    - N = 2 / Result = 3
    - N = 3 / Result = 5
    - N = 4 / Result = 11
    - N = 5 / Result = 21...
'''
