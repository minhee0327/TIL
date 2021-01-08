n, l, k = map(int, input().split())

easy, hard = 0, 0

for _ in range(n):
    sub1, sub2 = map(int, input().split())
    if sub2 <= l:
        hard += 1
    elif sub1 <= l:
        easy += 1

# hard문제 푸는 경우
ans = min(hard, k) * 140

# hard가 k보다 작으면 easy문제 더 풀수있음
# 내가풀수 있는문제 양 - hard, 쉬운문제수 중에 최소값만큼 더해줌.
if hard < k:
    ans += min(k-hard, easy)*100

print(ans)

'''
[Code Review]
- 일단 내가 엄청 복잡하게 풀었다는걸 강사님 코드를 보면서 느꼈다.
- (사실 속도, 공간측면은 동일했지만, 코드의 양이 엄청 적은게 놀라웠음.)

- 먼저, 나는 쉬운문제, 어려운문제를 위해 반복문을 두번 돌린 반면
- 강사님은 한번 반복문을 돌면서 조건을 체크해서 문제 수를 구하는 방식으로 진행했다.

- 구현을 하기 이전에, 조금 더 나은 방법이 생각난다면 한번 더 생각해보고 구현해보면 좋겠다는 생각을 했다.
- 반복되는 코드를 줄이기위해 생각하는 것도 연습이라고 생각한다.
'''
