# 런타임 에러 코드
T = int(input())

for _ in range(T):
    string = input()
    cusor = 0
    ans = []
    for i in range(len(string)):
        # print(cusor)
        if string[i] == '-':
            if ans[cusor-1] is not None:
                ans.remove(ans[cusor-1])
        elif string[i] == '<':
            if cusor > 0:
                cusor -= 1
            else:
                cusor = 0
        elif string[i] == '>':
            if cusor < len(ans):
                cusor += 1
            else:
                cusor = len(ans)
        else:
            ans.insert(cusor, string[i])
            cusor += 1
    print(''.join(ans))

'''
1. 위 내가 푼 방법은 런타임 에러를 내면서 끝났다.
(예전에도 그래놓고 또! 정신차리자)
- cusor를 이동하면서 주어진 조건에 맞게 입력했다고 생각했는데
- 출력값은 나왔지만 어딘가 문제가 있는 코드인 것 같다.
- 시간적으로도 불안하기는 했다.

2. 키로거 문제의 핵심은 
- 커서를 중심으로 좌, 우를 두고 생각해야한다는 점이다. 
- '-'일 때, 좌측에 값이 있다면 pop()해서 제거
- '<'일 때, 좌측에 값이 있다면 좌측에서 pop()한 값을 오른쪽에 붙이기
- '>'일 때, 오른쪽에 값이 있다면 우측에서 pop()한 값을 왼쪽에 붙이기.
- 나머지 문자일 경우, 좌측에 붙여주기

- 입력 받은 문자열 순회가 끝나면
    - 오른쪽 결과는 역순이므로 reverse를 해주어야 한다.
    - 왼쪽에서 확장해서 오른쪽 결과를 붙여주기.
- 출력

3. 이를 바탕으로 키로거2에 다시 풀어보아야겠다.
'''
