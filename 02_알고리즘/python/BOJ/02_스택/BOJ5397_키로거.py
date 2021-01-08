# 런타임 => 시간초과 => 해결 ㅠㅠ!
from sys import stdin
from collections import deque

for _ in range(int(stdin.readline())):
    string = stdin.readline().strip()
    cusor, cusor_len = 0, 0
    ans = deque()
    for s in string:
        # print(cusor)
        if s == '-':
            if cusor:
                del ans[cusor-1]
                cusor -= 1
                cusor_len -= 1
        elif s == '<':
            if cusor:
                cusor -= 1
        elif s == '>':
            if cusor < cusor_len:
                cusor += 1
        else:
            ans.insert(cusor, s)
            cusor += 1
            cusor_len += 1
    print(''.join(ans))

'''
1. 위 내가 푼 방법은 처음에 런타임 에러를 내면서 끝났다.
- cusor를 이동하면서 주어진 조건에 맞게 입력했다고 생각했는데
- 출력값은 나왔지만 어딘가 문제가 있는 코드인 것 같다.
- 시간적으로도 불안하기는 했다.(수정했더니 시간초과...)

2. 코드 개선하여 해결함
- 시간 부족한 문제는 2가지로 해결 
    - stdin.readline()으로
    - list대신 deque()로
- 런타임에러의 경우
    - 조건을 조금 수정함
    - '-'일 경우 삭제후, cursor를 앞으로 한칸 이동시켜주고, 총길이도 줄여준다.
    - cusor가 이동한 거리(cusor_len)을 생각 못했던 점이 error의 원인이었지 않나 싶다.

3. 키로거 문제의 핵심은
- 커서를 중심으로 좌, 우를 두고 생각해야한다는 점이다. 
- '-'일 때, 좌측에 값이 있다면 pop()해서 제거
- '<'일 때, 좌측에 값이 있다면 좌측에서 pop()한 값을 오른쪽에 붙이기
- '>'일 때, 오른쪽에 값이 있다면 우측에서 pop()한 값을 왼쪽에 붙이기.
- 나머지 문자일 경우, 좌측에 붙여주기

- 입력 받은 문자열 순회가 끝나면
    - 오른쪽 결과는 역순이므로 reverse를 해주어야 한다.
    - 왼쪽에서 확장해서 오른쪽 결과를 붙여주기.
- 출력

4. 총정
- 양방향 스택을 생각 못해냈는데, 다른 문제에도 접목할 수 있을 것 같다. 잘기억하자.
- 속도, 공간 문제가 생기면 꼭 stdin, deque등을 떠올려보자 해결 할 수도..!
 
'''
