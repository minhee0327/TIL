N = int(input())
switch = list(map(int, input().split()))

for _ in range(int(input())):
    S, num = map(int, input().split())
    if S == 1:
        k = num - 1
        while k < N:
            switch[k] = 1 - switch[k]
            k += num
    else:
        switch[num-1] = 1 - switch[num-1]

        for i in range(1, N-1):
            if num - 1 - i >= 0 and num - 1 + i < N and switch[num-1-i] == switch[num-1+i]:
                switch[num-1-i] = 1 - switch[num-1-i]
                switch[num-1+i] = 1 - switch[num-1+i]
            else:
                break

for i, e in enumerate(switch):
    if i and not (i % 20):
        print()
    print(e, end=" ")


'''
코드 수정
- 과정1
    - switch[k] = 1 - switch[k]
    - 원래는 나머지연산으로 계산했었다가
    - 반복문으로 해봤다가, 위 코드가 가장 깔끔한 것 같아 수정
- 과정 2
    - 출력부분, enumerate로 idx값 받아서 활용함
- 과정 3
    - index가 0보다 작아졌을경우와 N보다 커졌을 경우 그 부분을 한칸씩 더 줄였다.
'''
