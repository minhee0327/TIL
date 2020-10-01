def findMax(bottom, top):
    temp_dice = [i for i in range(1, 7)]
    temp_dice.remove(bottom)
    temp_dice.remove(top)
    return max(temp_dice)


n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
order = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

ans = 0

for i in range(6):
    bottom, top = dice[0][i], dice[0][order[i]]
    temp = 0
    temp += findMax(bottom, top)
    for j in range(1, n):
        bottom = top
        top = dice[j][order[dice[j].index(top)]]  # 이부분을 생각하는데 오래걸림
        temp += findMax(bottom, top)
    if ans < temp:
        ans = temp

print(ans)

'''
[Code Review]
- 처음에 order 를 배열로 두고 계산했는데, index out of range error를 처리하다가, dict로 받는게 편할거같아서 수정함

- 각 주사위 면 정보를 dice에 담아두고
- A,B,C,D,E,F면이 bottom일때, top의 값을 dict형태로 담음
- 맨 밑의 주사위의 모든 경우를 살펴보기로 함(그래서 6번 반복)
- 맨 밑의 주사위에 따라, bottom, top값을 결정할 수가 있고, 결정된 뒤 옆면들중 최댓값을 temp에 더해감
- 마지막 주사위까지 쌓은 후, temp 값이 최종 값보다 크다면 업데이트 해주고 결과 출력
'''
