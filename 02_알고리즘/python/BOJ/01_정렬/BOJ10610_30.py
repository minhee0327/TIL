N = input()

if sum(map(int, list(N))) % 3 == 0 and '0' in N:
    print(''.join(sorted(N, reverse=True)))
else:
    print(-1)

'''
- 3의 배수이면서, 0이 들어있을 때, 30의배수
- 이때 최대이면서 3의배수를 만족하도록하고 출력
- 나머지 경우는 만들 수 없는경우이므로 -1 출력
'''
